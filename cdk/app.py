import aws_cdk as cdk
from cdk.pangeo_forge_batch_stack import PangeoForgeBatchStack

app = cdk.App()
PangeoForgeBatchStack(app, "PangeoForgeBatchStack")
app.synth()