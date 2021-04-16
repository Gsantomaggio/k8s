import kfp
import kfp.dsl as dsl


@dsl.pipeline(name='my_after_parallel_pipe_line')
def pipeline(project_id='ai-test'):
    cont = dsl.ContainerOp(
        name='MyImage',
        image="ubuntu",
        command=['sh', '-c'],
        arguments=['ls'],
        # file_outputs={'output': '/tmp/output'},
    )
    cont.execution_options.caching_strategy.max_cache_staleness = "P0D"
    second = dsl.ContainerOp(
        name='Alpine Image',
        image="alpine",
        command=['sh', '-c'],
        arguments=["ls"],
    )
    second.after(cont)
    second.execution_options.caching_strategy.max_cache_staleness = "P0D"

    par = dsl.ContainerOp(
        name='Myparallel',
        image="ubuntu",
        command=['sh', '-c'],
        arguments=['ls'],
        # file_outputs={'output': '/tmp/output'},
    )
    par.execution_options.caching_strategy.max_cache_staleness = "P0D"
    par2 = dsl.ContainerOp(
        name='Alpine Image',
        image="alpine",
        command=['sh', '-c'],
        arguments=['touch', '/tmp/output'],
        file_outputs={'output': '/tmp/output'},
    )
    par2.after(par)
    par2.execution_options.caching_strategy.max_cache_staleness = "P0D"

    with dsl.Condition(par2.output <= 0):
        c = dsl.ContainerOp(
            name='TEST condition',
            image="ls",
            command=['sh', '-c'],
            arguments=["ls"],
        )
        c.execution_options.caching_strategy.max_cache_staleness = "P0D"
    with dsl.Condition(par2.output > 0):
        c = dsl.ContainerOp(
            name='TEST condition 2',
            image="ls",
            command=['sh', '-c'],
            arguments=["ls"],
        )
        c.execution_options.caching_strategy.max_cache_staleness = "P0D"

    dsl.get_pipeline_conf().set_ttl_seconds_after_finished(50)
