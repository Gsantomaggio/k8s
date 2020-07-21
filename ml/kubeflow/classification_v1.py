import kfp
import kfp.dsl as dsl


@dsl.pipeline(name='iris_classification')
def pipeline(project_id='ai-254012'):
    command = 'python3  iris_classification.py kf_decision_tree_test'
    image = "sklearn:v10"
    vop = dsl.VolumeOp(
        name="Create disk",
        resource_name="pipe-pvc",
        storage_class='standard',
        modes=dsl.VOLUME_MODE_RWO,
        size='1Gi'
    )

    data_tree = dsl.ContainerOp(
        name='TEST decision Tree',
        image=image,
        command=['sh', '-c'],
        arguments=[command],
        file_outputs={'output': '/tmp/output'},
    )
    data_tree.after(vop)

    data_tree.execution_options.caching_strategy.max_cache_staleness = "P0D"
    with dsl.Condition(data_tree.output <= 0.90):
        c = dsl.ContainerOp(
            name='TEST fail Decision Tree',
            image=image,
            command=['sh', '-c'],
            arguments=['ls'],
        )
        c.execution_options.caching_strategy.max_cache_staleness = "P0D"

    command = 'python3  iris_classification.py kf_decision_kneighbors_test'

    data_knc = dsl.ContainerOp(
        name='TEST decision KNC',
        image=image,
        command=['sh', '-c'],
        arguments=[command],
        file_outputs={'output': '/tmp/output'},
    )
    data_knc.execution_options.caching_strategy.max_cache_staleness = "P0D"
    data_knc.after(vop)

    with dsl.Condition(data_knc.output <= 0.90):
        c = dsl.ContainerOp(
            name='TEST fail decision KNC ',
            image=image,
            command=['sh', '-c'],
            arguments=["ls"],
        )
        c.execution_options.caching_strategy.max_cache_staleness = "P0D"

    with dsl.Condition(data_knc.output > data_tree.output):
        c = dsl.ContainerOp(
            name='Training KNC',
            image=image,
            command=['sh', '-c'],
            arguments=['python3  iris_classification.py decision_kneighbors && cp models/knc.pkl /mnt/model.pkl'],
            file_outputs={'output': '/mnt/model.pkl'},
            pvolumes={"/mnt": data_knc.pvolume}
        )
        c.execution_options.caching_strategy.max_cache_staleness = "P0D"

    with dsl.Condition(data_knc.output <= data_tree.output):
        c = dsl.ContainerOp(
            name='Training TREE',
            image=image,
            command=['sh', '-c'],
            arguments=['python3  iris_classification.py decision_tree && cp models/tree.pkl /mnt/model.pkl'],
            file_outputs={'output': '/mnt/model.pkl'},
            pvolumes={"/mnt": data_tree.pvolume}
        )
        c.execution_options.caching_strategy.max_cache_staleness = "P0D"

    dsl.get_pipeline_conf().set_ttl_seconds_after_finished(400)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline, __file__ + '.yaml')
