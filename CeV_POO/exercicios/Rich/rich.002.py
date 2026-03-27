from rich import print
from rich.panel import Panel

caixa = Panel(title='Mensagem', 
              title_align='left', 
              subtitle='msg',
              subtitle_align='left',
              safe_box=True,
              expand=False,
              style='white',
              border_style='red',
              width=25,
              height=10,
              highlight=True,
              renderable='Mensagem de teste'
              )

print(caixa)