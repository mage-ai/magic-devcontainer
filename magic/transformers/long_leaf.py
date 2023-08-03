from typing import Dict, List
import json

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(messages: List[Dict], *args, **kwargs):
    """
    Template code for a transformer block.

    Args:
        messages: List of messages in the stream.

    Returns:
        Transformed messages
    """

    transformed = [json.loads(m.get('data')) for m in messages]
    print(transformed[0])
    return transformed
