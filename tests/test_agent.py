import pytest
from ichatbio.agent_response import TextResponse, ProcessBeginResponse, ProcessLogResponse, ArtifactResponse

from src.agent import HelloWorldAgent


@pytest.mark.asyncio
async def test_hello_world(context, messages):
    # The test `context` populates the `messages` list with the agent's responses
    await HelloWorldAgent().run(context, "Hi", "hello", None)

    # Message objects are restricted to the following types:
    messages: list[TextResponse | ProcessBeginResponse | ProcessLogResponse | ArtifactResponse]

    # We can test all the agent's responses at once
    assert messages == [
        ProcessBeginResponse("Thinking"),
        ProcessLogResponse("Hello world!"),
        ArtifactResponse(mimetype="text/html",
                         description="The Wikipedia page for \"Hello World\"",
                         uris=["https://en.wikipedia.org/wiki/Hello_World"],
                         metadata={'source': 'Wikipedia'}),
        TextResponse("I said it!")
    ]
