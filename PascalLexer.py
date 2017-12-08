# Generated from antlr/Pascal.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2O")
        buf.write("\u0289\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\39\39\39")
        buf.write("\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3>\3?\3?\3?\3?\3?\3@\3@\3")
        buf.write("@\3@\3@\3@\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3")
        buf.write("C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3M\3M\3M\3N\3N\3O\3O\3O\3P\3P\3P\3Q\3Q\3R\3R\3S\3")
        buf.write("S\3T\3T\3U\3U\3U\3V\3V\3W\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3")
        buf.write("[\3[\3\\\3\\\3]\3]\3^\3^\3^\3^\3^\3_\3_\3_\3_\3_\3_\3")
        buf.write("_\3_\3_\3_\3`\3`\3`\3`\3`\3a\3a\3a\3a\3a\3a\3a\3b\3b\3")
        buf.write("b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3c\3c\3c\3c\3d\3")
        buf.write("d\3d\3d\7d\u0247\nd\fd\16d\u024a\13d\3d\3d\3d\3d\3d\3")
        buf.write("e\3e\7e\u0253\ne\fe\16e\u0256\13e\3e\3e\3e\3e\3f\3f\7")
        buf.write("f\u025e\nf\ff\16f\u0261\13f\3g\3g\3g\3g\7g\u0267\ng\f")
        buf.write("g\16g\u026a\13g\3g\3g\3h\6h\u026f\nh\rh\16h\u0270\3h\3")
        buf.write("h\6h\u0275\nh\rh\16h\u0276\3h\5h\u027a\nh\5h\u027c\nh")
        buf.write("\3h\5h\u027f\nh\3i\3i\5i\u0283\ni\3i\6i\u0286\ni\ri\16")
        buf.write("i\u0287\4\u0248\u0254\2j\3\2\5\2\7\2\t\2\13\2\r\2\17\2")
        buf.write("\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2")
        buf.write(")\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE\n")
        buf.write("G\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30")
        buf.write("c\31e\32g\33i\34k\35m\36o\37q s!u\"w#y${%}&\177\'\u0081")
        buf.write("(\u0083)\u0085*\u0087+\u0089,\u008b-\u008d.\u008f/\u0091")
        buf.write("\60\u0093\61\u0095\62\u0097\63\u0099\64\u009b\65\u009d")
        buf.write("\66\u009f\67\u00a18\u00a39\u00a5:\u00a7;\u00a9<\u00ab")
        buf.write("=\u00ad>\u00af?\u00b1@\u00b3A\u00b5B\u00b7C\u00b9D\u00bb")
        buf.write("E\u00bdF\u00bfG\u00c1H\u00c3I\u00c5J\u00c7K\u00c9L\u00cb")
        buf.write("M\u00cdN\u00cfO\u00d1\2\3\2!\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\5\2\13\f\17\17\"\"\4\2C\\c|\6")
        buf.write("\2\62;C\\aac|\3\2))\4\2--//\2\u0279\2\67\3\2\2\2\29\3")
        buf.write("\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C")
        buf.write("\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2")
        buf.write("M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2")
        buf.write("\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2")
        buf.write("\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2")
        buf.write("\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3")
        buf.write("\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2")
        buf.write("\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5")
        buf.write("\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2")
        buf.write("\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3")
        buf.write("\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2")
        buf.write("\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2\2\3\u00d3")
        buf.write("\3\2\2\2\5\u00d5\3\2\2\2\7\u00d7\3\2\2\2\t\u00d9\3\2\2")
        buf.write("\2\13\u00db\3\2\2\2\r\u00dd\3\2\2\2\17\u00df\3\2\2\2\21")
        buf.write("\u00e1\3\2\2\2\23\u00e3\3\2\2\2\25\u00e5\3\2\2\2\27\u00e7")
        buf.write("\3\2\2\2\31\u00e9\3\2\2\2\33\u00eb\3\2\2\2\35\u00ed\3")
        buf.write("\2\2\2\37\u00ef\3\2\2\2!\u00f1\3\2\2\2#\u00f3\3\2\2\2")
        buf.write("%\u00f5\3\2\2\2\'\u00f7\3\2\2\2)\u00f9\3\2\2\2+\u00fb")
        buf.write("\3\2\2\2-\u00fd\3\2\2\2/\u00ff\3\2\2\2\61\u0101\3\2\2")
        buf.write("\2\63\u0103\3\2\2\2\65\u0105\3\2\2\2\67\u0107\3\2\2\2")
        buf.write("9\u010b\3\2\2\2;\u0111\3\2\2\2=\u0117\3\2\2\2?\u011f\3")
        buf.write("\2\2\2A\u0124\3\2\2\2C\u0129\3\2\2\2E\u012d\3\2\2\2G\u0133")
        buf.write("\3\2\2\2I\u0137\3\2\2\2K\u013a\3\2\2\2M\u0141\3\2\2\2")
        buf.write("O\u0146\3\2\2\2Q\u014a\3\2\2\2S\u014f\3\2\2\2U\u0153\3")
        buf.write("\2\2\2W\u015c\3\2\2\2Y\u0161\3\2\2\2[\u0164\3\2\2\2]\u0167")
        buf.write("\3\2\2\2_\u016f\3\2\2\2a\u0175\3\2\2\2c\u0179\3\2\2\2")
        buf.write("e\u017d\3\2\2\2g\u0181\3\2\2\2i\u0184\3\2\2\2k\u0187\3")
        buf.write("\2\2\2m\u018e\3\2\2\2o\u0198\3\2\2\2q\u01a0\3\2\2\2s\u01a5")
        buf.write("\3\2\2\2u\u01ac\3\2\2\2w\u01b3\3\2\2\2y\u01b7\3\2\2\2")
        buf.write("{\u01bc\3\2\2\2}\u01bf\3\2\2\2\177\u01c4\3\2\2\2\u0081")
        buf.write("\u01ca\3\2\2\2\u0083\u01ce\3\2\2\2\u0085\u01d4\3\2\2\2")
        buf.write("\u0087\u01d9\3\2\2\2\u0089\u01db\3\2\2\2\u008b\u01dd\3")
        buf.write("\2\2\2\u008d\u01df\3\2\2\2\u008f\u01e1\3\2\2\2\u0091\u01e4")
        buf.write("\3\2\2\2\u0093\u01e6\3\2\2\2\u0095\u01e8\3\2\2\2\u0097")
        buf.write("\u01ea\3\2\2\2\u0099\u01ec\3\2\2\2\u009b\u01ef\3\2\2\2")
        buf.write("\u009d\u01f1\3\2\2\2\u009f\u01f4\3\2\2\2\u00a1\u01f7\3")
        buf.write("\2\2\2\u00a3\u01f9\3\2\2\2\u00a5\u01fb\3\2\2\2\u00a7\u01fd")
        buf.write("\3\2\2\2\u00a9\u01ff\3\2\2\2\u00ab\u0202\3\2\2\2\u00ad")
        buf.write("\u0204\3\2\2\2\u00af\u0207\3\2\2\2\u00b1\u0209\3\2\2\2")
        buf.write("\u00b3\u020b\3\2\2\2\u00b5\u020d\3\2\2\2\u00b7\u0210\3")
        buf.write("\2\2\2\u00b9\u0212\3\2\2\2\u00bb\u0214\3\2\2\2\u00bd\u0219")
        buf.write("\3\2\2\2\u00bf\u0223\3\2\2\2\u00c1\u0228\3\2\2\2\u00c3")
        buf.write("\u022f\3\2\2\2\u00c5\u023e\3\2\2\2\u00c7\u0242\3\2\2\2")
        buf.write("\u00c9\u0250\3\2\2\2\u00cb\u025b\3\2\2\2\u00cd\u0262\3")
        buf.write("\2\2\2\u00cf\u026e\3\2\2\2\u00d1\u0280\3\2\2\2\u00d3\u00d4")
        buf.write("\t\2\2\2\u00d4\4\3\2\2\2\u00d5\u00d6\t\3\2\2\u00d6\6\3")
        buf.write("\2\2\2\u00d7\u00d8\t\4\2\2\u00d8\b\3\2\2\2\u00d9\u00da")
        buf.write("\t\5\2\2\u00da\n\3\2\2\2\u00db\u00dc\t\6\2\2\u00dc\f\3")
        buf.write("\2\2\2\u00dd\u00de\t\7\2\2\u00de\16\3\2\2\2\u00df\u00e0")
        buf.write("\t\b\2\2\u00e0\20\3\2\2\2\u00e1\u00e2\t\t\2\2\u00e2\22")
        buf.write("\3\2\2\2\u00e3\u00e4\t\n\2\2\u00e4\24\3\2\2\2\u00e5\u00e6")
        buf.write("\t\13\2\2\u00e6\26\3\2\2\2\u00e7\u00e8\t\f\2\2\u00e8\30")
        buf.write("\3\2\2\2\u00e9\u00ea\t\r\2\2\u00ea\32\3\2\2\2\u00eb\u00ec")
        buf.write("\t\16\2\2\u00ec\34\3\2\2\2\u00ed\u00ee\t\17\2\2\u00ee")
        buf.write("\36\3\2\2\2\u00ef\u00f0\t\20\2\2\u00f0 \3\2\2\2\u00f1")
        buf.write("\u00f2\t\21\2\2\u00f2\"\3\2\2\2\u00f3\u00f4\t\22\2\2\u00f4")
        buf.write("$\3\2\2\2\u00f5\u00f6\t\23\2\2\u00f6&\3\2\2\2\u00f7\u00f8")
        buf.write("\t\24\2\2\u00f8(\3\2\2\2\u00f9\u00fa\t\25\2\2\u00fa*\3")
        buf.write("\2\2\2\u00fb\u00fc\t\26\2\2\u00fc,\3\2\2\2\u00fd\u00fe")
        buf.write("\t\27\2\2\u00fe.\3\2\2\2\u00ff\u0100\t\30\2\2\u0100\60")
        buf.write("\3\2\2\2\u0101\u0102\t\31\2\2\u0102\62\3\2\2\2\u0103\u0104")
        buf.write("\t\32\2\2\u0104\64\3\2\2\2\u0105\u0106\t\33\2\2\u0106")
        buf.write("\66\3\2\2\2\u0107\u0108\5\3\2\2\u0108\u0109\5\35\17\2")
        buf.write("\u0109\u010a\5\t\5\2\u010a8\3\2\2\2\u010b\u010c\5\3\2")
        buf.write("\2\u010c\u010d\5%\23\2\u010d\u010e\5%\23\2\u010e\u010f")
        buf.write("\5\3\2\2\u010f\u0110\5\63\32\2\u0110:\3\2\2\2\u0111\u0112")
        buf.write("\5\5\3\2\u0112\u0113\5\13\6\2\u0113\u0114\5\17\b\2\u0114")
        buf.write("\u0115\5\23\n\2\u0115\u0116\5\35\17\2\u0116<\3\2\2\2\u0117")
        buf.write("\u0118\5\5\3\2\u0118\u0119\5\37\20\2\u0119\u011a\5\37")
        buf.write("\20\2\u011a\u011b\5\31\r\2\u011b\u011c\5\13\6\2\u011c")
        buf.write("\u011d\5\3\2\2\u011d\u011e\5\35\17\2\u011e>\3\2\2\2\u011f")
        buf.write("\u0120\5\7\4\2\u0120\u0121\5\3\2\2\u0121\u0122\5\'\24")
        buf.write("\2\u0122\u0123\5\13\6\2\u0123@\3\2\2\2\u0124\u0125\5\7")
        buf.write("\4\2\u0125\u0126\5\21\t\2\u0126\u0127\5\3\2\2\u0127\u0128")
        buf.write("\5%\23\2\u0128B\3\2\2\2\u0129\u012a\5\7\4\2\u012a\u012b")
        buf.write("\5\21\t\2\u012b\u012c\5%\23\2\u012cD\3\2\2\2\u012d\u012e")
        buf.write("\5\7\4\2\u012e\u012f\5\37\20\2\u012f\u0130\5\35\17\2\u0130")
        buf.write("\u0131\5\'\24\2\u0131\u0132\5)\25\2\u0132F\3\2\2\2\u0133")
        buf.write("\u0134\5\t\5\2\u0134\u0135\5\23\n\2\u0135\u0136\5-\27")
        buf.write("\2\u0136H\3\2\2\2\u0137\u0138\5\t\5\2\u0138\u0139\5\37")
        buf.write("\20\2\u0139J\3\2\2\2\u013a\u013b\5\t\5\2\u013b\u013c\5")
        buf.write("\37\20\2\u013c\u013d\5/\30\2\u013d\u013e\5\35\17\2\u013e")
        buf.write("\u013f\5)\25\2\u013f\u0140\5\37\20\2\u0140L\3\2\2\2\u0141")
        buf.write("\u0142\5\13\6\2\u0142\u0143\5\31\r\2\u0143\u0144\5\'\24")
        buf.write("\2\u0144\u0145\5\13\6\2\u0145N\3\2\2\2\u0146\u0147\5\13")
        buf.write("\6\2\u0147\u0148\5\35\17\2\u0148\u0149\5\t\5\2\u0149P")
        buf.write("\3\2\2\2\u014a\u014b\5\r\7\2\u014b\u014c\5\23\n\2\u014c")
        buf.write("\u014d\5\31\r\2\u014d\u014e\5\13\6\2\u014eR\3\2\2\2\u014f")
        buf.write("\u0150\5\r\7\2\u0150\u0151\5\37\20\2\u0151\u0152\5%\23")
        buf.write("\2\u0152T\3\2\2\2\u0153\u0154\5\r\7\2\u0154\u0155\5+\26")
        buf.write("\2\u0155\u0156\5\35\17\2\u0156\u0157\5\7\4\2\u0157\u0158")
        buf.write("\5)\25\2\u0158\u0159\5\23\n\2\u0159\u015a\5\37\20\2\u015a")
        buf.write("\u015b\5\35\17\2\u015bV\3\2\2\2\u015c\u015d\5\17\b\2\u015d")
        buf.write("\u015e\5\37\20\2\u015e\u015f\5)\25\2\u015f\u0160\5\37")
        buf.write("\20\2\u0160X\3\2\2\2\u0161\u0162\5\23\n\2\u0162\u0163")
        buf.write("\5\r\7\2\u0163Z\3\2\2\2\u0164\u0165\5\23\n\2\u0165\u0166")
        buf.write("\5\35\17\2\u0166\\\3\2\2\2\u0167\u0168\5\23\n\2\u0168")
        buf.write("\u0169\5\35\17\2\u0169\u016a\5)\25\2\u016a\u016b\5\13")
        buf.write("\6\2\u016b\u016c\5\17\b\2\u016c\u016d\5\13\6\2\u016d\u016e")
        buf.write("\5%\23\2\u016e^\3\2\2\2\u016f\u0170\5\31\r\2\u0170\u0171")
        buf.write("\5\3\2\2\u0171\u0172\5\5\3\2\u0172\u0173\5\13\6\2\u0173")
        buf.write("\u0174\5\31\r\2\u0174`\3\2\2\2\u0175\u0176\5\33\16\2\u0176")
        buf.write("\u0177\5\37\20\2\u0177\u0178\5\t\5\2\u0178b\3\2\2\2\u0179")
        buf.write("\u017a\5\35\17\2\u017a\u017b\5\23\n\2\u017b\u017c\5\31")
        buf.write("\r\2\u017cd\3\2\2\2\u017d\u017e\5\35\17\2\u017e\u017f")
        buf.write("\5\37\20\2\u017f\u0180\5)\25\2\u0180f\3\2\2\2\u0181\u0182")
        buf.write("\5\37\20\2\u0182\u0183\5\r\7\2\u0183h\3\2\2\2\u0184\u0185")
        buf.write("\5\37\20\2\u0185\u0186\5%\23\2\u0186j\3\2\2\2\u0187\u0188")
        buf.write("\5!\21\2\u0188\u0189\5\3\2\2\u0189\u018a\5\7\4\2\u018a")
        buf.write("\u018b\5\27\f\2\u018b\u018c\5\13\6\2\u018c\u018d\5\t\5")
        buf.write("\2\u018dl\3\2\2\2\u018e\u018f\5!\21\2\u018f\u0190\5%\23")
        buf.write("\2\u0190\u0191\5\37\20\2\u0191\u0192\5\7\4\2\u0192\u0193")
        buf.write("\5\13\6\2\u0193\u0194\5\t\5\2\u0194\u0195\5+\26\2\u0195")
        buf.write("\u0196\5%\23\2\u0196\u0197\5\13\6\2\u0197n\3\2\2\2\u0198")
        buf.write("\u0199\5!\21\2\u0199\u019a\5%\23\2\u019a\u019b\5\37\20")
        buf.write("\2\u019b\u019c\5\17\b\2\u019c\u019d\5%\23\2\u019d\u019e")
        buf.write("\5\3\2\2\u019e\u019f\5\33\16\2\u019fp\3\2\2\2\u01a0\u01a1")
        buf.write("\5%\23\2\u01a1\u01a2\5\13\6\2\u01a2\u01a3\5\3\2\2\u01a3")
        buf.write("\u01a4\5\31\r\2\u01a4r\3\2\2\2\u01a5\u01a6\5%\23\2\u01a6")
        buf.write("\u01a7\5\13\6\2\u01a7\u01a8\5\7\4\2\u01a8\u01a9\5\37\20")
        buf.write("\2\u01a9\u01aa\5%\23\2\u01aa\u01ab\5\t\5\2\u01abt\3\2")
        buf.write("\2\2\u01ac\u01ad\5%\23\2\u01ad\u01ae\5\13\6\2\u01ae\u01af")
        buf.write("\5!\21\2\u01af\u01b0\5\13\6\2\u01b0\u01b1\5\3\2\2\u01b1")
        buf.write("\u01b2\5)\25\2\u01b2v\3\2\2\2\u01b3\u01b4\5\'\24\2\u01b4")
        buf.write("\u01b5\5\13\6\2\u01b5\u01b6\5)\25\2\u01b6x\3\2\2\2\u01b7")
        buf.write("\u01b8\5)\25\2\u01b8\u01b9\5\21\t\2\u01b9\u01ba\5\13\6")
        buf.write("\2\u01ba\u01bb\5\35\17\2\u01bbz\3\2\2\2\u01bc\u01bd\5")
        buf.write(")\25\2\u01bd\u01be\5\37\20\2\u01be|\3\2\2\2\u01bf\u01c0")
        buf.write("\5)\25\2\u01c0\u01c1\5\63\32\2\u01c1\u01c2\5!\21\2\u01c2")
        buf.write("\u01c3\5\13\6\2\u01c3~\3\2\2\2\u01c4\u01c5\5+\26\2\u01c5")
        buf.write("\u01c6\5\35\17\2\u01c6\u01c7\5)\25\2\u01c7\u01c8\5\23")
        buf.write("\n\2\u01c8\u01c9\5\31\r\2\u01c9\u0080\3\2\2\2\u01ca\u01cb")
        buf.write("\5-\27\2\u01cb\u01cc\5\3\2\2\u01cc\u01cd\5%\23\2\u01cd")
        buf.write("\u0082\3\2\2\2\u01ce\u01cf\5/\30\2\u01cf\u01d0\5\21\t")
        buf.write("\2\u01d0\u01d1\5\23\n\2\u01d1\u01d2\5\31\r\2\u01d2\u01d3")
        buf.write("\5\13\6\2\u01d3\u0084\3\2\2\2\u01d4\u01d5\5/\30\2\u01d5")
        buf.write("\u01d6\5\23\n\2\u01d6\u01d7\5)\25\2\u01d7\u01d8\5\21\t")
        buf.write("\2\u01d8\u0086\3\2\2\2\u01d9\u01da\7-\2\2\u01da\u0088")
        buf.write("\3\2\2\2\u01db\u01dc\7/\2\2\u01dc\u008a\3\2\2\2\u01dd")
        buf.write("\u01de\7,\2\2\u01de\u008c\3\2\2\2\u01df\u01e0\7\61\2\2")
        buf.write("\u01e0\u008e\3\2\2\2\u01e1\u01e2\7<\2\2\u01e2\u01e3\7")
        buf.write("?\2\2\u01e3\u0090\3\2\2\2\u01e4\u01e5\7.\2\2\u01e5\u0092")
        buf.write("\3\2\2\2\u01e6\u01e7\7=\2\2\u01e7\u0094\3\2\2\2\u01e8")
        buf.write("\u01e9\7<\2\2\u01e9\u0096\3\2\2\2\u01ea\u01eb\7?\2\2\u01eb")
        buf.write("\u0098\3\2\2\2\u01ec\u01ed\7>\2\2\u01ed\u01ee\7@\2\2\u01ee")
        buf.write("\u009a\3\2\2\2\u01ef\u01f0\7>\2\2\u01f0\u009c\3\2\2\2")
        buf.write("\u01f1\u01f2\7>\2\2\u01f2\u01f3\7?\2\2\u01f3\u009e\3\2")
        buf.write("\2\2\u01f4\u01f5\7@\2\2\u01f5\u01f6\7?\2\2\u01f6\u00a0")
        buf.write("\3\2\2\2\u01f7\u01f8\7@\2\2\u01f8\u00a2\3\2\2\2\u01f9")
        buf.write("\u01fa\7*\2\2\u01fa\u00a4\3\2\2\2\u01fb\u01fc\7+\2\2\u01fc")
        buf.write("\u00a6\3\2\2\2\u01fd\u01fe\7]\2\2\u01fe\u00a8\3\2\2\2")
        buf.write("\u01ff\u0200\7*\2\2\u0200\u0201\7\60\2\2\u0201\u00aa\3")
        buf.write("\2\2\2\u0202\u0203\7_\2\2\u0203\u00ac\3\2\2\2\u0204\u0205")
        buf.write("\7\60\2\2\u0205\u0206\7+\2\2\u0206\u00ae\3\2\2\2\u0207")
        buf.write("\u0208\7`\2\2\u0208\u00b0\3\2\2\2\u0209\u020a\7B\2\2\u020a")
        buf.write("\u00b2\3\2\2\2\u020b\u020c\7\60\2\2\u020c\u00b4\3\2\2")
        buf.write("\2\u020d\u020e\7\60\2\2\u020e\u020f\7\60\2\2\u020f\u00b6")
        buf.write("\3\2\2\2\u0210\u0211\7}\2\2\u0211\u00b8\3\2\2\2\u0212")
        buf.write("\u0213\7\177\2\2\u0213\u00ba\3\2\2\2\u0214\u0215\5+\26")
        buf.write("\2\u0215\u0216\5\35\17\2\u0216\u0217\5\23\n\2\u0217\u0218")
        buf.write("\5)\25\2\u0218\u00bc\3\2\2\2\u0219\u021a\5\23\n\2\u021a")
        buf.write("\u021b\5\35\17\2\u021b\u021c\5)\25\2\u021c\u021d\5\13")
        buf.write("\6\2\u021d\u021e\5%\23\2\u021e\u021f\5\r\7\2\u021f\u0220")
        buf.write("\5\3\2\2\u0220\u0221\5\7\4\2\u0221\u0222\5\13\6\2\u0222")
        buf.write("\u00be\3\2\2\2\u0223\u0224\5+\26\2\u0224\u0225\5\'\24")
        buf.write("\2\u0225\u0226\5\13\6\2\u0226\u0227\5\'\24\2\u0227\u00c0")
        buf.write("\3\2\2\2\u0228\u0229\5\'\24\2\u0229\u022a\5)\25\2\u022a")
        buf.write("\u022b\5%\23\2\u022b\u022c\5\23\n\2\u022c\u022d\5\35\17")
        buf.write("\2\u022d\u022e\5\17\b\2\u022e\u00c2\3\2\2\2\u022f\u0230")
        buf.write("\5\23\n\2\u0230\u0231\5\33\16\2\u0231\u0232\5!\21\2\u0232")
        buf.write("\u0233\5\31\r\2\u0233\u0234\5\13\6\2\u0234\u0235\5\33")
        buf.write("\16\2\u0235\u0236\5\13\6\2\u0236\u0237\5\35\17\2\u0237")
        buf.write("\u0238\5)\25\2\u0238\u0239\5\3\2\2\u0239\u023a\5)\25\2")
        buf.write("\u023a\u023b\5\23\n\2\u023b\u023c\5\37\20\2\u023c\u023d")
        buf.write("\5\35\17\2\u023d\u00c4\3\2\2\2\u023e\u023f\t\34\2\2\u023f")
        buf.write("\u0240\3\2\2\2\u0240\u0241\bc\2\2\u0241\u00c6\3\2\2\2")
        buf.write("\u0242\u0243\7*\2\2\u0243\u0244\7,\2\2\u0244\u0248\3\2")
        buf.write("\2\2\u0245\u0247\13\2\2\2\u0246\u0245\3\2\2\2\u0247\u024a")
        buf.write("\3\2\2\2\u0248\u0249\3\2\2\2\u0248\u0246\3\2\2\2\u0249")
        buf.write("\u024b\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024c\7,\2\2")
        buf.write("\u024c\u024d\7+\2\2\u024d\u024e\3\2\2\2\u024e\u024f\b")
        buf.write("d\2\2\u024f\u00c8\3\2\2\2\u0250\u0254\7}\2\2\u0251\u0253")
        buf.write("\13\2\2\2\u0252\u0251\3\2\2\2\u0253\u0256\3\2\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u0257\3\2\2\2")
        buf.write("\u0256\u0254\3\2\2\2\u0257\u0258\7\177\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u025a\be\2\2\u025a\u00ca\3\2\2\2\u025b")
        buf.write("\u025f\t\35\2\2\u025c\u025e\t\36\2\2\u025d\u025c\3\2\2")
        buf.write("\2\u025e\u0261\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u00cc\3\2\2\2\u0261\u025f\3\2\2\2\u0262")
        buf.write("\u0268\7)\2\2\u0263\u0264\7)\2\2\u0264\u0267\7)\2\2\u0265")
        buf.write("\u0267\n\37\2\2\u0266\u0263\3\2\2\2\u0266\u0265\3\2\2")
        buf.write("\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0268\u0269")
        buf.write("\3\2\2\2\u0269\u026b\3\2\2\2\u026a\u0268\3\2\2\2\u026b")
        buf.write("\u026c\7)\2\2\u026c\u00ce\3\2\2\2\u026d\u026f\4\62;\2")
        buf.write("\u026e\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0270\u0271\3\2\2\2\u0271\u027e\3\2\2\2\u0272\u0274")
        buf.write("\7\60\2\2\u0273\u0275\4\62;\2\u0274\u0273\3\2\2\2\u0275")
        buf.write("\u0276\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0279\3\2\2\2\u0278\u027a\5\u00d1i\2\u0279\u0278")
        buf.write("\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u027c\3\2\2\2\u027b")
        buf.write("\u0272\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027f\3\2\2\2")
        buf.write("\u027d\u027f\5\u00d1i\2\u027e\u027b\3\2\2\2\u027e\u027d")
        buf.write("\3\2\2\2\u027f\u00d0\3\2\2\2\u0280\u0282\7g\2\2\u0281")
        buf.write("\u0283\t \2\2\u0282\u0281\3\2\2\2\u0282\u0283\3\2\2\2")
        buf.write("\u0283\u0285\3\2\2\2\u0284\u0286\4\62;\2\u0285\u0284\3")
        buf.write("\2\2\2\u0286\u0287\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0288")
        buf.write("\3\2\2\2\u0288\u00d2\3\2\2\2\17\2\u0248\u0254\u025f\u0266")
        buf.write("\u0268\u0270\u0276\u0279\u027b\u027e\u0282\u0287\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class PascalLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    ARRAY = 2
    BEGIN = 3
    BOOLEAN = 4
    CASE = 5
    CHAR = 6
    CHR = 7
    CONST = 8
    DIV = 9
    DO = 10
    DOWNTO = 11
    ELSE = 12
    END = 13
    FILE = 14
    FOR = 15
    FUNCTION = 16
    GOTO = 17
    IF = 18
    IN = 19
    INTEGER = 20
    LABEL = 21
    MOD = 22
    NIL = 23
    NOT = 24
    OF = 25
    OR = 26
    PACKED = 27
    PROCEDURE = 28
    PROGRAM = 29
    REAL = 30
    RECORD = 31
    REPEAT = 32
    SET = 33
    THEN = 34
    TO = 35
    TYPE = 36
    UNTIL = 37
    VAR = 38
    WHILE = 39
    WITH = 40
    PLUS = 41
    MINUS = 42
    STAR = 43
    SLASH = 44
    ASSIGN = 45
    COMMA = 46
    SEMI = 47
    COLON = 48
    EQUAL = 49
    NOT_EQUAL = 50
    LT = 51
    LE = 52
    GE = 53
    GT = 54
    LPAREN = 55
    RPAREN = 56
    LBRACK = 57
    LBRACK2 = 58
    RBRACK = 59
    RBRACK2 = 60
    POINTER = 61
    AT = 62
    DOT = 63
    DOTDOT = 64
    LCURLY = 65
    RCURLY = 66
    UNIT = 67
    INTERFACE = 68
    USES = 69
    STRING = 70
    IMPLEMENTATION = 71
    WS = 72
    COMMENT_1 = 73
    COMMENT_2 = 74
    IDENT = 75
    STRING_LITERAL = 76
    NUM_INT = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "':='", "','", "';'", "':'", "'='", 
            "'<>'", "'<'", "'<='", "'>='", "'>'", "'('", "')'", "'['", "'(.'", 
            "']'", "'.)'", "'^'", "'@'", "'.'", "'..'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "ARRAY", "BEGIN", "BOOLEAN", "CASE", "CHAR", "CHR", "CONST", 
            "DIV", "DO", "DOWNTO", "ELSE", "END", "FILE", "FOR", "FUNCTION", 
            "GOTO", "IF", "IN", "INTEGER", "LABEL", "MOD", "NIL", "NOT", 
            "OF", "OR", "PACKED", "PROCEDURE", "PROGRAM", "REAL", "RECORD", 
            "REPEAT", "SET", "THEN", "TO", "TYPE", "UNTIL", "VAR", "WHILE", 
            "WITH", "PLUS", "MINUS", "STAR", "SLASH", "ASSIGN", "COMMA", 
            "SEMI", "COLON", "EQUAL", "NOT_EQUAL", "LT", "LE", "GE", "GT", 
            "LPAREN", "RPAREN", "LBRACK", "LBRACK2", "RBRACK", "RBRACK2", 
            "POINTER", "AT", "DOT", "DOTDOT", "LCURLY", "RCURLY", "UNIT", 
            "INTERFACE", "USES", "STRING", "IMPLEMENTATION", "WS", "COMMENT_1", 
            "COMMENT_2", "IDENT", "STRING_LITERAL", "NUM_INT" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "AND", "ARRAY", "BEGIN", "BOOLEAN", 
                  "CASE", "CHAR", "CHR", "CONST", "DIV", "DO", "DOWNTO", 
                  "ELSE", "END", "FILE", "FOR", "FUNCTION", "GOTO", "IF", 
                  "IN", "INTEGER", "LABEL", "MOD", "NIL", "NOT", "OF", "OR", 
                  "PACKED", "PROCEDURE", "PROGRAM", "REAL", "RECORD", "REPEAT", 
                  "SET", "THEN", "TO", "TYPE", "UNTIL", "VAR", "WHILE", 
                  "WITH", "PLUS", "MINUS", "STAR", "SLASH", "ASSIGN", "COMMA", 
                  "SEMI", "COLON", "EQUAL", "NOT_EQUAL", "LT", "LE", "GE", 
                  "GT", "LPAREN", "RPAREN", "LBRACK", "LBRACK2", "RBRACK", 
                  "RBRACK2", "POINTER", "AT", "DOT", "DOTDOT", "LCURLY", 
                  "RCURLY", "UNIT", "INTERFACE", "USES", "STRING", "IMPLEMENTATION", 
                  "WS", "COMMENT_1", "COMMENT_2", "IDENT", "STRING_LITERAL", 
                  "NUM_INT", "EXPONENT" ]

    grammarFileName = "Pascal.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


