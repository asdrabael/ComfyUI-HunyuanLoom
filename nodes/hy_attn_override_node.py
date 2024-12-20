
def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    

class HYAttnOverrideNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "double_blocks": ("STRING", { "multiline": True }),
                "single_blocks": ("STRING", { "multiline": True }),
            }
        }

    RETURN_TYPES = ("ATTN_OVERRIDE",)
    FUNCTION = "build"

    CATEGORY = "hunyuanloom/attn"

    def build(self, double_blocks, single_blocks):
        
        double_block_layers = { f'{i}': False for i in range(20) }
        double_block_map = set()
        for block in double_blocks.split(','):
            block = block.strip()
            if is_integer(block):
                double_block_map.add(block)
                double_block_layers[f'{block}'] = True
        
        single_block_layers = { f'{i}': False for i in range(40) }
        single_block_map = set()
        for block in single_blocks.split(','):
            block = block.strip()
            if is_integer(block):
                single_block_map.add(block)
                single_block_layers[f'{block}'] = True

        return ({ "double": double_block_map, "single": single_block_map },)
    
