import kfp
import kfp.dsl as dsl


@dsl.pipeline(name='my_second_pipe_line')
def pipeline(project_id='ai-254012'):
    cont = dsl.ContainerOp(
        name='MyImage',
        image="ubuntu",
        command=['sh', '-c'],
        arguments=['ls'],
        # file_outputs={'output': '/tmp/output'},
    )
    cont.execution_options.caching_strategy.max_cache_staleness = "P0D"
    dsl.get_pipeline_conf().set_ttl_seconds_after_finished(15)
