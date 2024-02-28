class StringNode:
  
  @classmethod
  def INPUT_TYPES(cls): 
    return {
      "required": {        
        "textA": ("STRING", {"multiline": True,"default": ""}),     
        "textB": ("STRING", {"multiline": True,"default": ""}),   
        "textC": ("STRING", {"multiline": True,"default": ""}),   
        },

      }

  RETURN_TYPES = ('STRING',)
  RETURN_NAMES = ('combin_text',)
  OUTPUT_NODE = True
  
  FUNCTION = "output"
  CATEGORY = "ecjojo_example"

  def output(self, textA,textB,textC):
      text = textA +","+ textB +","+ textC
      return {text}