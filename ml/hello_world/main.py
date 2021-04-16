import kfp
import kfp.dsl as dsl


@dsl.pipeline(name='my_first_pipe_line')
def pipeline(project_id='ai-254012'):
    dsl.ContainerOp(
        name='MyImage',
        image="ubuntu",
        command=['sh', '-c'],
        arguments=['ls'],
        # file_outputs={'output': '/tmp/output'},
    )
