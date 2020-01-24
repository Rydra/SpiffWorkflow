from spiffworkflow.specs import WorkflowSpec
from spiffworkflow.serializer.json import JSONSerializer

serializer = JSONSerializer()
with open('workflow-spec.json') as fp:
    workflow_json = fp.read()
spec = WorkflowSpec.deserialize(serializer, workflow_json)
