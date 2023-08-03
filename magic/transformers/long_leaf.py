from typing import Dict, List
import json

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(messages: List[Dict], *args, **kwargs):
    """
    Google sends us messages like {'data':'stringified_json'} 🙈
    Let's clean it up! 🧹
    """
    transformed = [json.loads(m.get('data')) for m in messages]
    
    print(transformed[0])
    
    return transformed
