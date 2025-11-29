from PyQt5.QtWidgets import *
from node_graphics_scene import QDMGraphicsScene
class NodeEditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200,200,800,600)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

        # Graphic Scene
        self.scene = QDMGraphicsScene(self)

        # Graphic View
        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        self.layout.addWidget(self.view)

        self.setWindowTitle('ReMiD-Node Editor')  
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = NodeEditorWindow()
    sys.exit(app.exec_())
