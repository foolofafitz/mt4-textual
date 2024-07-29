from rich.text import Text

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, HorizontalScroll
from textual.widgets import Static, Label, DataTable, ListItem

ROWS = [
        ("EURUSD", 1, "SHORT 0.14", 80.59),
        ("AUDUSD", 1, "LONG 14", -9880.59),
        ("GBPUSD", 10, "LONG 2", 1000),
        ]

class SymbolItem(ListItem):
    DEFAULT_CSS = """
    .box {
        width: 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        with HorizontalScroll():
            yield Static("Symbol")
            yield Static("Orders")
            yield Static("Position")
            yield Static("Lots")
            yield Static("Profit")

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.add_column("Symbol")
        table.add_column("Orders")
        table.add_column("Position", key="Position")
        table.add_column("Profit")

        for row in ROWS:
            styled_row = [
                    Text(str(cell), justify="center") for cell in row
                    ]
            #table.add_row(*styled_row, key=row[0])
            table.add_row(*row)
        table.sort("Position")

if __name__ == "__main__":
    app = MyApp()
    app.run()
