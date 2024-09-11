import flet as ft
from flet_core.icons import TEXT_FIELDS

def main(page: ft.Page):
        
        page.title="suma de 2 numero"
        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.bgcolor="blue"
        
        lbl1=ft.Text("suma de 2 numero",
                    style=ft.TextStyle(size=40,weight="bold"))
        
        ing1=ft.Image(src="west.png",width=200,height=200)
        
        page.add(
            ft.Column(
                [
                    lbl1,
                    ing1,
                    ft.Row([btnSi,btnNo],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
            )
        )

ft.app(main)

        
        
        
        
        
        
        
        
        
        
        
ft.app(main)
