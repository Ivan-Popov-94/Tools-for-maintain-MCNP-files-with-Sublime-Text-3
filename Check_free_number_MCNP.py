# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_IRISIxSLDT.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Iris_reloading(object):
    def setupUi(self, Iris_reloading):
        if Iris_reloading.objectName():
            Iris_reloading.setObjectName(u"Iris_reloading")
        Iris_reloading.resize(669, 483)
        Iris_reloading.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/iris_icon.png", QSize(), QIcon.Normal, QIcon.On)
        Iris_reloading.setWindowIcon(icon)
        self.open_file = QAction(Iris_reloading)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setEnabled(True)
        self.create_file = QAction(Iris_reloading)
        self.create_file.setObjectName(u"create_file")
        self.save_maps_file = QAction(Iris_reloading)
        self.save_maps_file.setObjectName(u"save_maps_file")
        self.help = QAction(Iris_reloading)
        self.help.setObjectName(u"help")
        self.about = QAction(Iris_reloading)
        self.about.setObjectName(u"about")
        self.save_order_file = QAction(Iris_reloading)
        self.save_order_file.setObjectName(u"save_order_file")
        self.close = QAction(Iris_reloading)
        self.close.setObjectName(u"close")
        self.centralwidget = QWidget(Iris_reloading)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        brush = QBrush(QColor(255, 255, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(85, 170, 0));
        __qtablewidgetitem1.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon1 = QIcon()
        icon1.addFile(u"L:/\u0420\u0410\u0411\u041e\u0422\u0410/iris_map_processing/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setBackground(QColor(255, 0, 255));
        __qtablewidgetitem2.setIcon(icon1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(255, 255, 0));
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(255, 170, 255));
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        icon2 = QIcon()
        icon2.addFile(u"L:/\u0420\u0410\u0411\u041e\u0422\u0410/iris_map_processing/iris_icon.png", QSize(), QIcon.Active, QIcon.On)
        font = QFont()
        font.setKerning(False)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font);
        __qtablewidgetitem6.setIcon(icon2);
        __qtablewidgetitem6.setFlags(Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(255, 85, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setBackground(brush3);
        __qtablewidgetitem8.setForeground(brush2);
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 0, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QRect(70, 80, 112, 120))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setFocusPolicy(Qt.StrongFocus)
        self.tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(-3)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(19)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.tableWidget.verticalHeader().setDefaultSectionSize(19)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(540, 50, 21, 171))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 10, 171, 31))
        palette = QPalette()
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush4 = QBrush(QColor(255, 170, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush4)
        brush5 = QBrush(QColor(85, 255, 127, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush4)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pushButton.setPalette(palette)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 25, 47, 13))
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setEnabled(False)
        self.textBrowser_2.setGeometry(QRect(70, 20, 251, 21))
        self.textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(530, 10, 61, 41))
        self.label_2.setWordWrap(True)
        self.xyi = QLabel(self.centralwidget)
        self.xyi.setObjectName(u"xyi")
        self.xyi.setGeometry(QRect(230, 130, 181, 151))
        self.xyi.setMouseTracking(True)
        self.xyi.setPixmap(QPixmap(u"L:/\u0420\u0410\u0411\u041e\u0422\u0410/iris_map_processing/fuck.png"))
        self.press_me = QPushButton(self.centralwidget)
        self.press_me.setObjectName(u"press_me")
        self.press_me.setGeometry(QRect(130, 330, 75, 23))
        Iris_reloading.setCentralWidget(self.centralwidget)
        self.tableWidget.raise_()
        self.textBrowser.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.textBrowser_2.raise_()
        self.xyi.raise_()
        self.press_me.raise_()
        self.menubar = QMenuBar(Iris_reloading)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 669, 21))
        self.menubar.setTabletTracking(False)
        self.menubar.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.menubar.setToolTipDuration(1)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(True)
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.file_menu.setCursor(QCursor(Qt.ArrowCursor))
        self.file_menu.setToolTipDuration(1)
        self.file_menu.setLayoutDirection(Qt.LeftToRight)
        self.help_about = QMenu(self.menubar)
        self.help_about.setObjectName(u"help_about")
        Iris_reloading.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Iris_reloading)
        self.statusbar.setObjectName(u"statusbar")
        Iris_reloading.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.help_about.menuAction())
        self.file_menu.addAction(self.open_file)
        self.file_menu.addAction(self.create_file)
        self.file_menu.addAction(self.save_maps_file)
        self.file_menu.addAction(self.save_order_file)
        self.file_menu.addAction(self.close)
        self.help_about.addAction(self.help)
        self.help_about.addAction(self.about)

        self.retranslateUi(Iris_reloading)
        self.close.triggered.connect(self.textBrowser_2.close)
        self.press_me.clicked.connect(self.textBrowser.setFocus)

        QMetaObject.connectSlotsByName(Iris_reloading)
    # setupUi

    def retranslateUi(self, Iris_reloading):
        Iris_reloading.setWindowTitle(QCoreApplication.translate("Iris_reloading", u"IRIS_reloading", None))
        self.open_file.setText(QCoreApplication.translate("Iris_reloading", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043c\u043f\u043e\u043d\u043e\u0432\u043e\u043a", None))
#if QT_CONFIG(shortcut)
        self.open_file.setShortcut(QCoreApplication.translate("Iris_reloading", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.create_file.setText(QCoreApplication.translate("Iris_reloading", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043c\u043f\u043e\u043d\u043e\u0432\u043e\u043a", None))
#if QT_CONFIG(shortcut)
        self.create_file.setShortcut(QCoreApplication.translate("Iris_reloading", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.save_maps_file.setText(QCoreApplication.translate("Iris_reloading", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u043a\u043e\u043c\u043f\u043e\u043d\u043e\u0432\u043e\u043a", None))
#if QT_CONFIG(shortcut)
        self.save_maps_file.setShortcut(QCoreApplication.translate("Iris_reloading", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.help.setText(QCoreApplication.translate("Iris_reloading", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
#if QT_CONFIG(shortcut)
        self.help.setShortcut(QCoreApplication.translate("Iris_reloading", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.about.setText(QCoreApplication.translate("Iris_reloading", u"about_program", None))
        self.save_order_file.setText(QCoreApplication.translate("Iris_reloading", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u043f\u0435\u0440\u0435\u0433\u0440\u0443\u0437\u043e\u043a", None))
        self.close.setText(QCoreApplication.translate("Iris_reloading", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Iris_reloading", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Iris_reloading", u"2", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Iris_reloading", u"3", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        ___qtablewidgetitem9 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Iris_reloading", u"1", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Iris_reloading", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("Iris_reloading", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.label_2.setText(QCoreApplication.translate("Iris_reloading", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u043f\u0435\u0440\u0435\u0433\u0440\u0443\u0437\u043e\u043a", None))
        self.xyi.setText("")
        self.press_me.setText(QCoreApplication.translate("Iris_reloading", u"\u043d\u0430\u0436\u043c\u0438 \u043c\u0435\u043d\u044f", None))
        self.file_menu.setTitle(QCoreApplication.translate("Iris_reloading", u"\u0424\u0430\u0439\u043b", None))
        self.help_about.setTitle(QCoreApplication.translate("Iris_reloading", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

