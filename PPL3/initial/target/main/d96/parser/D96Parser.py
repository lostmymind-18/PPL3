# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0277\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a2\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b2")
        buf.write("\n\4\3\5\3\5\5\5\u00b6\n\5\3\6\3\6\3\6\3\6\5\6\u00bc\n")
        buf.write("\6\3\7\3\7\3\7\3\7\5\7\u00c2\n\7\3\b\3\b\3\b\5\b\u00c7")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00d9\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00e0\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00e7\n\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\5\r\u00ef\n\r\3\16\3\16\3\16\5\16")
        buf.write("\u00f4\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u0105\n\23\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\5\25\u010d\n\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\5\32\u0128\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u012f")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u013f\n\35\3\36\3\36\3\36\5")
        buf.write("\36\u0144\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0158\n \3!\3!\3!\3!\5")
        buf.write("!\u015e\n!\3\"\3\"\3\"\3\"\3\"\3#\3#\5#\u0167\n#\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\5&\u0177\n&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u0182\n(\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\5*\u0192\n*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\5-\u019c\n-\3-\3-\3.\3.\3.\3.\3.\5.\u01a5")
        buf.write("\n.\3.\3.\3.\3/\3/\3/\3/\3/\5/\u01af\n/\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\61\3\61\5\61\u01ba\n\61\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01c0\n\62\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01c7\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u01ce\n\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u01d7\n\65\f\65")
        buf.write("\16\65\u01da\13\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\7\66\u01e3\n\66\f\66\16\66\u01e6\13\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\7\67\u01ef\n\67\f\67\16\67\u01f2")
        buf.write("\13\67\38\38\38\38\58\u01f8\n8\39\39\39\59\u01fd\n9\3")
        buf.write(":\3:\3:\3:\3:\3:\5:\u0205\n:\3;\3;\3;\3;\3;\3;\3;\3;\7")
        buf.write(";\u020f\n;\f;\16;\u0212\13;\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\5<\u021f\n<\3<\7<\u0222\n<\f<\16<\u0225\13<\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\5=\u022f\n=\3=\3=\5=\u0233\n=\3")
        buf.write(">\3>\3>\3>\5>\u0239\n>\3>\3>\5>\u023d\n>\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\5?\u0246\n?\3@\3@\3@\3@\3@\3@\5@\u024e\n@\3A\3")
        buf.write("A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3J\3J\3J\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\5L\u0271\nL\3")
        buf.write("M\3M\5M\u0275\nM\3M\2\7hjltvN\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\2\13\4\2\20")
        buf.write("\20\25\25\6\2\5\5\n\n\17\17\24\24\4\2!!%%\7\2  $$((+,")
        buf.write("//\4\2##\'\'\4\2\36\36\"\"\5\2&&**--\3\2\34\35\4\2\t\t")
        buf.write("\16\16\2\u0271\2\u009a\3\2\2\2\4\u00a1\3\2\2\2\6\u00b1")
        buf.write("\3\2\2\2\b\u00b5\3\2\2\2\n\u00bb\3\2\2\2\f\u00c1\3\2\2")
        buf.write("\2\16\u00c3\3\2\2\2\20\u00c8\3\2\2\2\22\u00d8\3\2\2\2")
        buf.write("\24\u00df\3\2\2\2\26\u00e6\3\2\2\2\30\u00ee\3\2\2\2\32")
        buf.write("\u00f3\3\2\2\2\34\u00f5\3\2\2\2\36\u00f7\3\2\2\2 \u00f9")
        buf.write("\3\2\2\2\"\u00fe\3\2\2\2$\u0104\3\2\2\2&\u0106\3\2\2\2")
        buf.write("(\u010c\3\2\2\2*\u010e\3\2\2\2,\u0114\3\2\2\2.\u011a\3")
        buf.write("\2\2\2\60\u0120\3\2\2\2\62\u0127\3\2\2\2\64\u012e\3\2")
        buf.write("\2\2\66\u0130\3\2\2\28\u013e\3\2\2\2:\u0140\3\2\2\2<\u0147")
        buf.write("\3\2\2\2>\u0157\3\2\2\2@\u015d\3\2\2\2B\u015f\3\2\2\2")
        buf.write("D\u0166\3\2\2\2F\u0168\3\2\2\2H\u016b\3\2\2\2J\u0176\3")
        buf.write("\2\2\2L\u0178\3\2\2\2N\u0181\3\2\2\2P\u0183\3\2\2\2R\u0191")
        buf.write("\3\2\2\2T\u0193\3\2\2\2V\u0196\3\2\2\2X\u0199\3\2\2\2")
        buf.write("Z\u019f\3\2\2\2\\\u01a9\3\2\2\2^\u01b3\3\2\2\2`\u01b9")
        buf.write("\3\2\2\2b\u01bf\3\2\2\2d\u01c6\3\2\2\2f\u01cd\3\2\2\2")
        buf.write("h\u01cf\3\2\2\2j\u01db\3\2\2\2l\u01e7\3\2\2\2n\u01f7\3")
        buf.write("\2\2\2p\u01fc\3\2\2\2r\u0204\3\2\2\2t\u0206\3\2\2\2v\u0213")
        buf.write("\3\2\2\2x\u0232\3\2\2\2z\u023c\3\2\2\2|\u0245\3\2\2\2")
        buf.write("~\u024d\3\2\2\2\u0080\u024f\3\2\2\2\u0082\u0251\3\2\2")
        buf.write("\2\u0084\u0253\3\2\2\2\u0086\u0255\3\2\2\2\u0088\u0257")
        buf.write("\3\2\2\2\u008a\u0259\3\2\2\2\u008c\u025b\3\2\2\2\u008e")
        buf.write("\u025d\3\2\2\2\u0090\u025f\3\2\2\2\u0092\u0261\3\2\2\2")
        buf.write("\u0094\u0266\3\2\2\2\u0096\u0270\3\2\2\2\u0098\u0274\3")
        buf.write("\2\2\2\u009a\u009b\5\4\3\2\u009b\u009c\7\2\2\3\u009c\3")
        buf.write("\3\2\2\2\u009d\u009e\5\6\4\2\u009e\u009f\5\4\3\2\u009f")
        buf.write("\u00a2\3\2\2\2\u00a0\u00a2\5\6\4\2\u00a1\u009d\3\2\2\2")
        buf.write("\u00a1\u00a0\3\2\2\2\u00a2\5\3\2\2\2\u00a3\u00a4\7\13")
        buf.write("\2\2\u00a4\u00a5\7\34\2\2\u00a5\u00a6\7\62\2\2\u00a6\u00a7")
        buf.write("\5\b\5\2\u00a7\u00a8\7\63\2\2\u00a8\u00b2\3\2\2\2\u00a9")
        buf.write("\u00aa\7\13\2\2\u00aa\u00ab\7\34\2\2\u00ab\u00ac\78\2")
        buf.write("\2\u00ac\u00ad\7\34\2\2\u00ad\u00ae\7\62\2\2\u00ae\u00af")
        buf.write("\5\b\5\2\u00af\u00b0\7\63\2\2\u00b0\u00b2\3\2\2\2\u00b1")
        buf.write("\u00a3\3\2\2\2\u00b1\u00a9\3\2\2\2\u00b2\7\3\2\2\2\u00b3")
        buf.write("\u00b6\5\n\6\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b4\3\2\2\2\u00b6\t\3\2\2\2\u00b7\u00b8\5\f\7")
        buf.write("\2\u00b8\u00b9\5\n\6\2\u00b9\u00bc\3\2\2\2\u00ba\u00bc")
        buf.write("\5\f\7\2\u00bb\u00b7\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc")
        buf.write("\13\3\2\2\2\u00bd\u00be\5\16\b\2\u00be\u00bf\7\64\2\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00c2\5(\25\2\u00c1\u00bd\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\r\3\2\2\2\u00c3\u00c6")
        buf.write("\t\2\2\2\u00c4\u00c7\5\20\t\2\u00c5\u00c7\5\22\n\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\17\3\2\2\2\u00c8")
        buf.write("\u00c9\5\24\13\2\u00c9\u00ca\78\2\2\u00ca\u00cb\5\32\16")
        buf.write("\2\u00cb\21\3\2\2\2\u00cc\u00cd\5\u008eH\2\u00cd\u00ce")
        buf.write("\7\65\2\2\u00ce\u00cf\5\22\n\2\u00cf\u00d0\7\65\2\2\u00d0")
        buf.write("\u00d1\5d\63\2\u00d1\u00d9\3\2\2\2\u00d2\u00d3\5\u008e")
        buf.write("H\2\u00d3\u00d4\78\2\2\u00d4\u00d5\5\32\16\2\u00d5\u00d6")
        buf.write("\7.\2\2\u00d6\u00d7\5d\63\2\u00d7\u00d9\3\2\2\2\u00d8")
        buf.write("\u00cc\3\2\2\2\u00d8\u00d2\3\2\2\2\u00d9\23\3\2\2\2\u00da")
        buf.write("\u00db\5\u008eH\2\u00db\u00dc\7\65\2\2\u00dc\u00dd\5\24")
        buf.write("\13\2\u00dd\u00e0\3\2\2\2\u00de\u00e0\5\u008eH\2\u00df")
        buf.write("\u00da\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\25\3\2\2\2\u00e1")
        buf.write("\u00e2\5d\63\2\u00e2\u00e3\7\65\2\2\u00e3\u00e4\5\26\f")
        buf.write("\2\u00e4\u00e7\3\2\2\2\u00e5\u00e7\5d\63\2\u00e6\u00e1")
        buf.write("\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\27\3\2\2\2\u00e8\u00ef")
        buf.write("\7<\2\2\u00e9\u00ef\7=\2\2\u00ea\u00ef\5\u0090I\2\u00eb")
        buf.write("\u00ef\7>\2\2\u00ec\u00ef\5\u0092J\2\u00ed\u00ef\5\u0094")
        buf.write("K\2\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee\u00ea")
        buf.write("\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee")
        buf.write("\u00ed\3\2\2\2\u00ef\31\3\2\2\2\u00f0\u00f4\5\36\20\2")
        buf.write("\u00f1\u00f4\5 \21\2\u00f2\u00f4\5\34\17\2\u00f3\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4")
        buf.write("\33\3\2\2\2\u00f5\u00f6\7\34\2\2\u00f6\35\3\2\2\2\u00f7")
        buf.write("\u00f8\t\3\2\2\u00f8\37\3\2\2\2\u00f9\u00fa\7\23\2\2\u00fa")
        buf.write("\u00fb\7\66\2\2\u00fb\u00fc\5\"\22\2\u00fc\u00fd\7\67")
        buf.write("\2\2\u00fd!\3\2\2\2\u00fe\u00ff\5$\23\2\u00ff\u0100\7")
        buf.write("\65\2\2\u0100\u0101\5&\24\2\u0101#\3\2\2\2\u0102\u0105")
        buf.write("\5\36\20\2\u0103\u0105\5 \21\2\u0104\u0102\3\2\2\2\u0104")
        buf.write("\u0103\3\2\2\2\u0105%\3\2\2\2\u0106\u0107\5d\63\2\u0107")
        buf.write("\'\3\2\2\2\u0108\u010d\5*\26\2\u0109\u010d\5,\27\2\u010a")
        buf.write("\u010d\5.\30\2\u010b\u010d\5\60\31\2\u010c\u0108\3\2\2")
        buf.write("\2\u010c\u0109\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010b")
        buf.write("\3\2\2\2\u010d)\3\2\2\2\u010e\u010f\7\35\2\2\u010f\u0110")
        buf.write("\7\60\2\2\u0110\u0111\5\62\32\2\u0111\u0112\7\61\2\2\u0112")
        buf.write("\u0113\5^\60\2\u0113+\3\2\2\2\u0114\u0115\7\34\2\2\u0115")
        buf.write("\u0116\7\60\2\2\u0116\u0117\5\62\32\2\u0117\u0118\7\61")
        buf.write("\2\2\u0118\u0119\5^\60\2\u0119-\3\2\2\2\u011a\u011b\7")
        buf.write("\7\2\2\u011b\u011c\7\60\2\2\u011c\u011d\5\62\32\2\u011d")
        buf.write("\u011e\7\61\2\2\u011e\u011f\5^\60\2\u011f/\3\2\2\2\u0120")
        buf.write("\u0121\7\f\2\2\u0121\u0122\7\60\2\2\u0122\u0123\7\61\2")
        buf.write("\2\u0123\u0124\5^\60\2\u0124\61\3\2\2\2\u0125\u0128\5")
        buf.write("\64\33\2\u0126\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0127")
        buf.write("\u0126\3\2\2\2\u0128\63\3\2\2\2\u0129\u012a\5\66\34\2")
        buf.write("\u012a\u012b\7\64\2\2\u012b\u012c\5\64\33\2\u012c\u012f")
        buf.write("\3\2\2\2\u012d\u012f\5\66\34\2\u012e\u0129\3\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\65\3\2\2\2\u0130\u0131\5@!\2\u0131")
        buf.write("\u0132\78\2\2\u0132\u0133\5\32\16\2\u0133\67\3\2\2\2\u0134")
        buf.write("\u013f\5:\36\2\u0135\u013f\5B\"\2\u0136\u013f\5F$\2\u0137")
        buf.write("\u013f\5P)\2\u0138\u013f\5T+\2\u0139\u013f\5V,\2\u013a")
        buf.write("\u013f\5X-\2\u013b\u013f\5\\/\2\u013c\u013f\5Z.\2\u013d")
        buf.write("\u013f\5^\60\2\u013e\u0134\3\2\2\2\u013e\u0135\3\2\2\2")
        buf.write("\u013e\u0136\3\2\2\2\u013e\u0137\3\2\2\2\u013e\u0138\3")
        buf.write("\2\2\2\u013e\u0139\3\2\2\2\u013e\u013a\3\2\2\2\u013e\u013b")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("9\3\2\2\2\u0140\u0143\t\2\2\2\u0141\u0144\5<\37\2\u0142")
        buf.write("\u0144\5> \2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0146\7\64\2\2\u0146;\3\2\2\2\u0147")
        buf.write("\u0148\5@!\2\u0148\u0149\78\2\2\u0149\u014a\5\32\16\2")
        buf.write("\u014a=\3\2\2\2\u014b\u014c\7\34\2\2\u014c\u014d\7\65")
        buf.write("\2\2\u014d\u014e\5> \2\u014e\u014f\7\65\2\2\u014f\u0150")
        buf.write("\5d\63\2\u0150\u0158\3\2\2\2\u0151\u0152\7\34\2\2\u0152")
        buf.write("\u0153\78\2\2\u0153\u0154\5\32\16\2\u0154\u0155\7.\2\2")
        buf.write("\u0155\u0156\5d\63\2\u0156\u0158\3\2\2\2\u0157\u014b\3")
        buf.write("\2\2\2\u0157\u0151\3\2\2\2\u0158?\3\2\2\2\u0159\u015a")
        buf.write("\7\34\2\2\u015a\u015b\7\65\2\2\u015b\u015e\5@!\2\u015c")
        buf.write("\u015e\7\34\2\2\u015d\u0159\3\2\2\2\u015d\u015c\3\2\2")
        buf.write("\2\u015eA\3\2\2\2\u015f\u0160\5D#\2\u0160\u0161\7.\2\2")
        buf.write("\u0161\u0162\5d\63\2\u0162\u0163\7\64\2\2\u0163C\3\2\2")
        buf.write("\2\u0164\u0167\5\u008eH\2\u0165\u0167\5r:\2\u0166\u0164")
        buf.write("\3\2\2\2\u0166\u0165\3\2\2\2\u0167E\3\2\2\2\u0168\u0169")
        buf.write("\5H%\2\u0169\u016a\5J&\2\u016aG\3\2\2\2\u016b\u016c\7")
        buf.write("\r\2\2\u016c\u016d\7\60\2\2\u016d\u016e\5d\63\2\u016e")
        buf.write("\u016f\7\61\2\2\u016f\u0170\5^\60\2\u0170I\3\2\2\2\u0171")
        buf.write("\u0172\5L\'\2\u0172\u0173\5J&\2\u0173\u0177\3\2\2\2\u0174")
        buf.write("\u0177\5N(\2\u0175\u0177\3\2\2\2\u0176\u0171\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177K\3\2\2\2\u0178")
        buf.write("\u0179\7\22\2\2\u0179\u017a\7\60\2\2\u017a\u017b\5d\63")
        buf.write("\2\u017b\u017c\7\61\2\2\u017c\u017d\5^\60\2\u017dM\3\2")
        buf.write("\2\2\u017e\u017f\7\27\2\2\u017f\u0182\5^\60\2\u0180\u0182")
        buf.write("\3\2\2\2\u0181\u017e\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("O\3\2\2\2\u0183\u0184\7\4\2\2\u0184\u0185\7\60\2\2\u0185")
        buf.write("\u0186\5\u008eH\2\u0186\u0187\7\30\2\2\u0187\u0188\5d")
        buf.write("\63\2\u0188\u0189\7;\2\2\u0189\u018a\5d\63\2\u018a\u018b")
        buf.write("\5R*\2\u018b\u018c\7\61\2\2\u018c\u018d\5^\60\2\u018d")
        buf.write("Q\3\2\2\2\u018e\u018f\7\26\2\2\u018f\u0192\5d\63\2\u0190")
        buf.write("\u0192\3\2\2\2\u0191\u018e\3\2\2\2\u0191\u0190\3\2\2\2")
        buf.write("\u0192S\3\2\2\2\u0193\u0194\7\3\2\2\u0194\u0195\7\64\2")
        buf.write("\2\u0195U\3\2\2\2\u0196\u0197\7\b\2\2\u0197\u0198\7\64")
        buf.write("\2\2\u0198W\3\2\2\2\u0199\u019b\7\31\2\2\u019a\u019c\5")
        buf.write("d\63\2\u019b\u019a\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019e\7\64\2\2\u019eY\3\2\2\2\u019f\u01a0")
        buf.write("\7\34\2\2\u01a0\u01a1\79\2\2\u01a1\u01a2\7\35\2\2\u01a2")
        buf.write("\u01a4\7\60\2\2\u01a3\u01a5\5\26\f\2\u01a4\u01a3\3\2\2")
        buf.write("\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7")
        buf.write("\7\61\2\2\u01a7\u01a8\7\64\2\2\u01a8[\3\2\2\2\u01a9\u01aa")
        buf.write("\5t;\2\u01aa\u01ab\7)\2\2\u01ab\u01ac\7\34\2\2\u01ac\u01ae")
        buf.write("\7\60\2\2\u01ad\u01af\5\26\f\2\u01ae\u01ad\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\7\61\2")
        buf.write("\2\u01b1\u01b2\7\64\2\2\u01b2]\3\2\2\2\u01b3\u01b4\7\62")
        buf.write("\2\2\u01b4\u01b5\5`\61\2\u01b5\u01b6\7\63\2\2\u01b6_\3")
        buf.write("\2\2\2\u01b7\u01ba\5b\62\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01b9\u01b8\3\2\2\2\u01baa\3\2\2\2\u01bb\u01bc")
        buf.write("\58\35\2\u01bc\u01bd\5b\62\2\u01bd\u01c0\3\2\2\2\u01be")
        buf.write("\u01c0\58\35\2\u01bf\u01bb\3\2\2\2\u01bf\u01be\3\2\2\2")
        buf.write("\u01c0c\3\2\2\2\u01c1\u01c2\5f\64\2\u01c2\u01c3\5\u0080")
        buf.write("A\2\u01c3\u01c4\5f\64\2\u01c4\u01c7\3\2\2\2\u01c5\u01c7")
        buf.write("\5f\64\2\u01c6\u01c1\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("e\3\2\2\2\u01c8\u01c9\5h\65\2\u01c9\u01ca\5\u0082B\2\u01ca")
        buf.write("\u01cb\5h\65\2\u01cb\u01ce\3\2\2\2\u01cc\u01ce\5h\65\2")
        buf.write("\u01cd\u01c8\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ceg\3\2\2")
        buf.write("\2\u01cf\u01d0\b\65\1\2\u01d0\u01d1\5j\66\2\u01d1\u01d8")
        buf.write("\3\2\2\2\u01d2\u01d3\f\4\2\2\u01d3\u01d4\5\u0084C\2\u01d4")
        buf.write("\u01d5\5j\66\2\u01d5\u01d7\3\2\2\2\u01d6\u01d2\3\2\2\2")
        buf.write("\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3")
        buf.write("\2\2\2\u01d9i\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dc")
        buf.write("\b\66\1\2\u01dc\u01dd\5l\67\2\u01dd\u01e4\3\2\2\2\u01de")
        buf.write("\u01df\f\4\2\2\u01df\u01e0\5\u0086D\2\u01e0\u01e1\5l\67")
        buf.write("\2\u01e1\u01e3\3\2\2\2\u01e2\u01de\3\2\2\2\u01e3\u01e6")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5")
        buf.write("k\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\b\67\1\2\u01e8")
        buf.write("\u01e9\5n8\2\u01e9\u01f0\3\2\2\2\u01ea\u01eb\f\4\2\2\u01eb")
        buf.write("\u01ec\5\u0088E\2\u01ec\u01ed\5n8\2\u01ed\u01ef\3\2\2")
        buf.write("\2\u01ee\u01ea\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1m\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f3\u01f4\5\u008aF\2\u01f4\u01f5\5n8\2\u01f5")
        buf.write("\u01f8\3\2\2\2\u01f6\u01f8\5p9\2\u01f7\u01f3\3\2\2\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8o\3\2\2\2\u01f9\u01fa\7\"\2\2\u01fa")
        buf.write("\u01fd\5p9\2\u01fb\u01fd\5r:\2\u01fc\u01f9\3\2\2\2\u01fc")
        buf.write("\u01fb\3\2\2\2\u01fdq\3\2\2\2\u01fe\u01ff\5t;\2\u01ff")
        buf.write("\u0200\7\66\2\2\u0200\u0201\5d\63\2\u0201\u0202\7\67\2")
        buf.write("\2\u0202\u0205\3\2\2\2\u0203\u0205\5v<\2\u0204\u01fe\3")
        buf.write("\2\2\2\u0204\u0203\3\2\2\2\u0205s\3\2\2\2\u0206\u0207")
        buf.write("\b;\1\2\u0207\u0208\5v<\2\u0208\u0210\3\2\2\2\u0209\u020a")
        buf.write("\f\4\2\2\u020a\u020b\7\66\2\2\u020b\u020c\5d\63\2\u020c")
        buf.write("\u020d\7\67\2\2\u020d\u020f\3\2\2\2\u020e\u0209\3\2\2")
        buf.write("\2\u020f\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211")
        buf.write("\3\2\2\2\u0211u\3\2\2\2\u0212\u0210\3\2\2\2\u0213\u0214")
        buf.write("\b<\1\2\u0214\u0215\5x=\2\u0215\u0223\3\2\2\2\u0216\u0217")
        buf.write("\f\5\2\2\u0217\u0218\7)\2\2\u0218\u0222\7\34\2\2\u0219")
        buf.write("\u021a\f\4\2\2\u021a\u021b\7)\2\2\u021b\u021c\7\34\2\2")
        buf.write("\u021c\u021e\7\60\2\2\u021d\u021f\5\26\f\2\u021e\u021d")
        buf.write("\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u0222\7\61\2\2\u0221\u0216\3\2\2\2\u0221\u0219\3\2\2")
        buf.write("\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224w\3\2\2\2\u0225\u0223\3\2\2\2\u0226\u0227")
        buf.write("\7\34\2\2\u0227\u0228\79\2\2\u0228\u0233\7\35\2\2\u0229")
        buf.write("\u022a\7\34\2\2\u022a\u022b\79\2\2\u022b\u022c\7\35\2")
        buf.write("\2\u022c\u022e\7\60\2\2\u022d\u022f\5\26\f\2\u022e\u022d")
        buf.write("\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\u0233\7\61\2\2\u0231\u0233\5z>\2\u0232\u0226\3\2\2\2")
        buf.write("\u0232\u0229\3\2\2\2\u0232\u0231\3\2\2\2\u0233y\3\2\2")
        buf.write("\2\u0234\u0235\7\21\2\2\u0235\u0236\7\34\2\2\u0236\u0238")
        buf.write("\7\60\2\2\u0237\u0239\5\26\f\2\u0238\u0237\3\2\2\2\u0238")
        buf.write("\u0239\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023d\7\61\2")
        buf.write("\2\u023b\u023d\5|?\2\u023c\u0234\3\2\2\2\u023c\u023b\3")
        buf.write("\2\2\2\u023d{\3\2\2\2\u023e\u0246\5\u008eH\2\u023f\u0246")
        buf.write("\5~@\2\u0240\u0241\7\60\2\2\u0241\u0242\5d\63\2\u0242")
        buf.write("\u0243\7\61\2\2\u0243\u0246\3\2\2\2\u0244\u0246\7\32\2")
        buf.write("\2\u0245\u023e\3\2\2\2\u0245\u023f\3\2\2\2\u0245\u0240")
        buf.write("\3\2\2\2\u0245\u0244\3\2\2\2\u0246}\3\2\2\2\u0247\u024e")
        buf.write("\7<\2\2\u0248\u024e\7>\2\2\u0249\u024e\7=\2\2\u024a\u024e")
        buf.write("\5\u0090I\2\u024b\u024e\5\u0092J\2\u024c\u024e\5\u0094")
        buf.write("K\2\u024d\u0247\3\2\2\2\u024d\u0248\3\2\2\2\u024d\u0249")
        buf.write("\3\2\2\2\u024d\u024a\3\2\2\2\u024d\u024b\3\2\2\2\u024d")
        buf.write("\u024c\3\2\2\2\u024e\177\3\2\2\2\u024f\u0250\t\4\2\2\u0250")
        buf.write("\u0081\3\2\2\2\u0251\u0252\t\5\2\2\u0252\u0083\3\2\2\2")
        buf.write("\u0253\u0254\t\6\2\2\u0254\u0085\3\2\2\2\u0255\u0256\t")
        buf.write("\7\2\2\u0256\u0087\3\2\2\2\u0257\u0258\t\b\2\2\u0258\u0089")
        buf.write("\3\2\2\2\u0259\u025a\7\37\2\2\u025a\u008b\3\2\2\2\u025b")
        buf.write("\u025c\7\21\2\2\u025c\u008d\3\2\2\2\u025d\u025e\t\t\2")
        buf.write("\2\u025e\u008f\3\2\2\2\u025f\u0260\t\n\2\2\u0260\u0091")
        buf.write("\3\2\2\2\u0261\u0262\7\23\2\2\u0262\u0263\7\60\2\2\u0263")
        buf.write("\u0264\5\26\f\2\u0264\u0265\7\61\2\2\u0265\u0093\3\2\2")
        buf.write("\2\u0266\u0267\7\23\2\2\u0267\u0268\7\60\2\2\u0268\u0269")
        buf.write("\5\u0096L\2\u0269\u026a\7\61\2\2\u026a\u0095\3\2\2\2\u026b")
        buf.write("\u026c\5\u0098M\2\u026c\u026d\7\65\2\2\u026d\u026e\5\u0096")
        buf.write("L\2\u026e\u0271\3\2\2\2\u026f\u0271\5\u0098M\2\u0270\u026b")
        buf.write("\3\2\2\2\u0270\u026f\3\2\2\2\u0271\u0097\3\2\2\2\u0272")
        buf.write("\u0275\5\u0094K\2\u0273\u0275\5\u0092J\2\u0274\u0272\3")
        buf.write("\2\2\2\u0274\u0273\3\2\2\2\u0275\u0099\3\2\2\2\62\u00a1")
        buf.write("\u00b1\u00b5\u00bb\u00c1\u00c6\u00d8\u00df\u00e6\u00ee")
        buf.write("\u00f3\u0104\u010c\u0127\u012e\u013e\u0143\u0157\u015d")
        buf.write("\u0166\u0176\u0181\u0191\u019b\u01a4\u01ae\u01b9\u01bf")
        buf.write("\u01c6\u01cd\u01d8\u01e4\u01f0\u01f7\u01fc\u0204\u0210")
        buf.write("\u021e\u0221\u0223\u022e\u0232\u0238\u023c\u0245\u024d")
        buf.write("\u0270\u0274")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'!'", "'!='", "'==.'", "'-'", "'&&'", "'>'", 
                     "'+.'", "'*'", "'||'", "'<='", "'.'", "'/'", "'=='", 
                     "'<'", "'%'", "'='", "'>='", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "'['", "']'", "':'", "'::'", "'$'", "'..'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "FOREACH", "INT", "NULL", "CONSTRUCTOR", 
                      "CONTINUE", "TRUE", "FLOAT", "CLASS", "DESTRUCTOR", 
                      "IF", "FALSE", "BOOLEAN", "VAL", "NEW", "ELSEIF", 
                      "ARRAY", "STRING", "VAR", "BY", "ELSE", "IN", "RETURN", 
                      "SELF", "BLOCK_COMM", "ID", "ID_STATIC", "PLUS", "EXCL", 
                      "DIF", "EQUA_DOT", "MINUS", "AND", "MOREE", "PLUS_DOT", 
                      "MUL", "OR", "LESS_EQUA", "DOT", "DIV", "EQUA", "LESS", 
                      "PERCENT", "ASS", "MORE_EQUA", "LB", "RB", "LP", "RP", 
                      "SEMI", "COMMA", "LS", "RS", "COLON", "DCOLON", "DOLLAR", 
                      "DDOT", "LIT_INT", "LIT_FLOAT", "LIT_STRING", "WS", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_list_class = 1
    RULE_class_decl = 2
    RULE_class_block = 3
    RULE_list_class_mem = 4
    RULE_class_mem_decl = 5
    RULE_class_attr_decl = 6
    RULE_attr1 = 7
    RULE_attr2 = 8
    RULE_list_id = 9
    RULE_list_expr = 10
    RULE_literal = 11
    RULE_mptype = 12
    RULE_class_type = 13
    RULE_primitive_type = 14
    RULE_array_type = 15
    RULE_array_characteristic = 16
    RULE_array_element_type = 17
    RULE_array_size = 18
    RULE_class_method_decl = 19
    RULE_static_method = 20
    RULE_instance_method = 21
    RULE_constructor_method = 22
    RULE_destructor_method = 23
    RULE_list_para = 24
    RULE_notnull_list_para = 25
    RULE_para = 26
    RULE_stat = 27
    RULE_stat_var_con = 28
    RULE_stat_var_con1 = 29
    RULE_stat_var_con2 = 30
    RULE_list_id_ins = 31
    RULE_stat_assign = 32
    RULE_stat_assign_lhs = 33
    RULE_stat_if = 34
    RULE_part_if = 35
    RULE_list_else = 36
    RULE_elseif = 37
    RULE_part_else = 38
    RULE_stat_foreach = 39
    RULE_by_expr = 40
    RULE_stat_break = 41
    RULE_stat_continue = 42
    RULE_stat_return = 43
    RULE_stat_method_sta = 44
    RULE_stat_method_ins = 45
    RULE_stat_block = 46
    RULE_block_body = 47
    RULE_list_stat = 48
    RULE_expr = 49
    RULE_expr1 = 50
    RULE_expr2 = 51
    RULE_expr3 = 52
    RULE_expr4 = 53
    RULE_expr5 = 54
    RULE_expr6 = 55
    RULE_expr7 = 56
    RULE_expr8 = 57
    RULE_expr9 = 58
    RULE_expr10 = 59
    RULE_expr11 = 60
    RULE_factor = 61
    RULE_lit = 62
    RULE_op_string = 63
    RULE_op_rel = 64
    RULE_op_log2 = 65
    RULE_op_add = 66
    RULE_op_mul = 67
    RULE_op_log1 = 68
    RULE_op_obj = 69
    RULE_mpid = 70
    RULE_lit_boolean = 71
    RULE_lit_indexed_arr = 72
    RULE_lit_mul_arr = 73
    RULE_mul_arr_elements = 74
    RULE_mul_arr_element = 75

    ruleNames =  [ "program", "list_class", "class_decl", "class_block", 
                   "list_class_mem", "class_mem_decl", "class_attr_decl", 
                   "attr1", "attr2", "list_id", "list_expr", "literal", 
                   "mptype", "class_type", "primitive_type", "array_type", 
                   "array_characteristic", "array_element_type", "array_size", 
                   "class_method_decl", "static_method", "instance_method", 
                   "constructor_method", "destructor_method", "list_para", 
                   "notnull_list_para", "para", "stat", "stat_var_con", 
                   "stat_var_con1", "stat_var_con2", "list_id_ins", "stat_assign", 
                   "stat_assign_lhs", "stat_if", "part_if", "list_else", 
                   "elseif", "part_else", "stat_foreach", "by_expr", "stat_break", 
                   "stat_continue", "stat_return", "stat_method_sta", "stat_method_ins", 
                   "stat_block", "block_body", "list_stat", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "expr10", "expr11", "factor", "lit", 
                   "op_string", "op_rel", "op_log2", "op_add", "op_mul", 
                   "op_log1", "op_obj", "mpid", "lit_boolean", "lit_indexed_arr", 
                   "lit_mul_arr", "mul_arr_elements", "mul_arr_element" ]

    EOF = Token.EOF
    BREAK=1
    FOREACH=2
    INT=3
    NULL=4
    CONSTRUCTOR=5
    CONTINUE=6
    TRUE=7
    FLOAT=8
    CLASS=9
    DESTRUCTOR=10
    IF=11
    FALSE=12
    BOOLEAN=13
    VAL=14
    NEW=15
    ELSEIF=16
    ARRAY=17
    STRING=18
    VAR=19
    BY=20
    ELSE=21
    IN=22
    RETURN=23
    SELF=24
    BLOCK_COMM=25
    ID=26
    ID_STATIC=27
    PLUS=28
    EXCL=29
    DIF=30
    EQUA_DOT=31
    MINUS=32
    AND=33
    MOREE=34
    PLUS_DOT=35
    MUL=36
    OR=37
    LESS_EQUA=38
    DOT=39
    DIV=40
    EQUA=41
    LESS=42
    PERCENT=43
    ASS=44
    MORE_EQUA=45
    LB=46
    RB=47
    LP=48
    RP=49
    SEMI=50
    COMMA=51
    LS=52
    RS=53
    COLON=54
    DCOLON=55
    DOLLAR=56
    DDOT=57
    LIT_INT=58
    LIT_FLOAT=59
    LIT_STRING=60
    WS=61
    ILLEGAL_ESCAPE=62
    UNCLOSE_STRING=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_class(self):
            return self.getTypedRuleContext(D96Parser.List_classContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.list_class()
            self.state = 153
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_declContext,0)


        def list_class(self):
            return self.getTypedRuleContext(D96Parser.List_classContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_class" ):
                return visitor.visitList_class(self)
            else:
                return visitor.visitChildren(self)




    def list_class(self):

        localctx = D96Parser.List_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_class)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.class_decl()
                self.state = 156
                self.list_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.class_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def class_block(self):
            return self.getTypedRuleContext(D96Parser.Class_blockContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_decl)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(D96Parser.CLASS)
                self.state = 162
                self.match(D96Parser.ID)
                self.state = 163
                self.match(D96Parser.LP)
                self.state = 164
                self.class_block()
                self.state = 165
                self.match(D96Parser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(D96Parser.CLASS)
                self.state = 168
                self.match(D96Parser.ID)
                self.state = 169
                self.match(D96Parser.COLON)
                self.state = 170
                self.match(D96Parser.ID)
                self.state = 171
                self.match(D96Parser.LP)
                self.state = 172
                self.class_block()
                self.state = 173
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_class_mem(self):
            return self.getTypedRuleContext(D96Parser.List_class_memContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_block" ):
                return visitor.visitClass_block(self)
            else:
                return visitor.visitChildren(self)




    def class_block(self):

        localctx = D96Parser.Class_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_block)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.VAL, D96Parser.VAR, D96Parser.ID, D96Parser.ID_STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.list_class_mem()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_class_memContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_mem_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_mem_declContext,0)


        def list_class_mem(self):
            return self.getTypedRuleContext(D96Parser.List_class_memContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_class_mem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_class_mem" ):
                return visitor.visitList_class_mem(self)
            else:
                return visitor.visitChildren(self)




    def list_class_mem(self):

        localctx = D96Parser.List_class_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_class_mem)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.class_mem_decl()
                self.state = 182
                self.list_class_mem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.class_mem_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_mem_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_attr_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_attr_declContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def class_method_decl(self):
            return self.getTypedRuleContext(D96Parser.Class_method_declContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_mem_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_mem_decl" ):
                return visitor.visitClass_mem_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_mem_decl(self):

        localctx = D96Parser.Class_mem_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_class_mem_decl)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.class_attr_decl()
                self.state = 188
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.ID_STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.class_method_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_attr_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def attr1(self):
            return self.getTypedRuleContext(D96Parser.Attr1Context,0)


        def attr2(self):
            return self.getTypedRuleContext(D96Parser.Attr2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_attr_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_attr_decl" ):
                return visitor.visitClass_attr_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_attr_decl(self):

        localctx = D96Parser.Class_attr_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_class_attr_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 194
                self.attr1()
                pass

            elif la_ == 2:
                self.state = 195
                self.attr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_id(self):
            return self.getTypedRuleContext(D96Parser.List_idContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr1" ):
                return visitor.visitAttr1(self)
            else:
                return visitor.visitChildren(self)




    def attr1(self):

        localctx = D96Parser.Attr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.list_id()
            self.state = 199
            self.match(D96Parser.COLON)
            self.state = 200
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mpid(self):
            return self.getTypedRuleContext(D96Parser.MpidContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attr2(self):
            return self.getTypedRuleContext(D96Parser.Attr2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def ASS(self):
            return self.getToken(D96Parser.ASS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr2" ):
                return visitor.visitAttr2(self)
            else:
                return visitor.visitChildren(self)




    def attr2(self):

        localctx = D96Parser.Attr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr2)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.mpid()
                self.state = 203
                self.match(D96Parser.COMMA)
                self.state = 204
                self.attr2()
                self.state = 205
                self.match(D96Parser.COMMA)
                self.state = 206
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.mpid()
                self.state = 209
                self.match(D96Parser.COLON)
                self.state = 210
                self.mptype()
                self.state = 211
                self.match(D96Parser.ASS)
                self.state = 212
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mpid(self):
            return self.getTypedRuleContext(D96Parser.MpidContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_id(self):
            return self.getTypedRuleContext(D96Parser.List_idContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_id" ):
                return visitor.visitList_id(self)
            else:
                return visitor.visitChildren(self)




    def list_id(self):

        localctx = D96Parser.List_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_id)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.mpid()
                self.state = 217
                self.match(D96Parser.COMMA)
                self.state = 218
                self.list_id()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.mpid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = D96Parser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.expr()
                self.state = 224
                self.match(D96Parser.COMMA)
                self.state = 225
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIT_INT(self):
            return self.getToken(D96Parser.LIT_INT, 0)

        def LIT_FLOAT(self):
            return self.getToken(D96Parser.LIT_FLOAT, 0)

        def lit_boolean(self):
            return self.getTypedRuleContext(D96Parser.Lit_booleanContext,0)


        def LIT_STRING(self):
            return self.getToken(D96Parser.LIT_STRING, 0)

        def lit_indexed_arr(self):
            return self.getTypedRuleContext(D96Parser.Lit_indexed_arrContext,0)


        def lit_mul_arr(self):
            return self.getTypedRuleContext(D96Parser.Lit_mul_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(D96Parser.LIT_INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(D96Parser.LIT_FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.lit_boolean()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.match(D96Parser.LIT_STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.lit_indexed_arr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 235
                self.lit_mul_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mptype)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def array_characteristic(self):
            return self.getTypedRuleContext(D96Parser.Array_characteristicContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(D96Parser.ARRAY)
            self.state = 248
            self.match(D96Parser.LS)
            self.state = 249
            self.array_characteristic()
            self.state = 250
            self.match(D96Parser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_characteristicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element_type(self):
            return self.getTypedRuleContext(D96Parser.Array_element_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def array_size(self):
            return self.getTypedRuleContext(D96Parser.Array_sizeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_characteristic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_characteristic" ):
                return visitor.visitArray_characteristic(self)
            else:
                return visitor.visitChildren(self)




    def array_characteristic(self):

        localctx = D96Parser.Array_characteristicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_characteristic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.array_element_type()
            self.state = 253
            self.match(D96Parser.COMMA)
            self.state = 254
            self.array_size()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_type" ):
                return visitor.visitArray_element_type(self)
            else:
                return visitor.visitChildren(self)




    def array_element_type(self):

        localctx = D96Parser.Array_element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_element_type)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = D96Parser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_method(self):
            return self.getTypedRuleContext(D96Parser.Static_methodContext,0)


        def instance_method(self):
            return self.getTypedRuleContext(D96Parser.Instance_methodContext,0)


        def constructor_method(self):
            return self.getTypedRuleContext(D96Parser.Constructor_methodContext,0)


        def destructor_method(self):
            return self.getTypedRuleContext(D96Parser.Destructor_methodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_method_decl" ):
                return visitor.visitClass_method_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_method_decl(self):

        localctx = D96Parser.Class_method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_class_method_decl)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID_STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.static_method()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.instance_method()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.constructor_method()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 265
                self.destructor_method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_para(self):
            return self.getTypedRuleContext(D96Parser.List_paraContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = D96Parser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_static_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(D96Parser.ID_STATIC)
            self.state = 269
            self.match(D96Parser.LB)
            self.state = 270
            self.list_para()
            self.state = 271
            self.match(D96Parser.RB)
            self.state = 272
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_para(self):
            return self.getTypedRuleContext(D96Parser.List_paraContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = D96Parser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_instance_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(D96Parser.ID)
            self.state = 275
            self.match(D96Parser.LB)
            self.state = 276
            self.list_para()
            self.state = 277
            self.match(D96Parser.RB)
            self.state = 278
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_para(self):
            return self.getTypedRuleContext(D96Parser.List_paraContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_method" ):
                return visitor.visitConstructor_method(self)
            else:
                return visitor.visitChildren(self)




    def constructor_method(self):

        localctx = D96Parser.Constructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_constructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 281
            self.match(D96Parser.LB)
            self.state = 282
            self.list_para()
            self.state = 283
            self.match(D96Parser.RB)
            self.state = 284
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_method" ):
                return visitor.visitDestructor_method(self)
            else:
                return visitor.visitChildren(self)




    def destructor_method(self):

        localctx = D96Parser.Destructor_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_destructor_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(D96Parser.DESTRUCTOR)
            self.state = 287
            self.match(D96Parser.LB)
            self.state = 288
            self.match(D96Parser.RB)
            self.state = 289
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notnull_list_para(self):
            return self.getTypedRuleContext(D96Parser.Notnull_list_paraContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = D96Parser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_para)
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.notnull_list_para()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Notnull_list_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(D96Parser.ParaContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def notnull_list_para(self):
            return self.getTypedRuleContext(D96Parser.Notnull_list_paraContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_notnull_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotnull_list_para" ):
                return visitor.visitNotnull_list_para(self)
            else:
                return visitor.visitChildren(self)




    def notnull_list_para(self):

        localctx = D96Parser.Notnull_list_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_notnull_list_para)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.para()
                self.state = 296
                self.match(D96Parser.SEMI)
                self.state = 297
                self.notnull_list_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.para()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_id_ins(self):
            return self.getTypedRuleContext(D96Parser.List_id_insContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = D96Parser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.list_id_ins()
            self.state = 303
            self.match(D96Parser.COLON)
            self.state = 304
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_var_con(self):
            return self.getTypedRuleContext(D96Parser.Stat_var_conContext,0)


        def stat_assign(self):
            return self.getTypedRuleContext(D96Parser.Stat_assignContext,0)


        def stat_if(self):
            return self.getTypedRuleContext(D96Parser.Stat_ifContext,0)


        def stat_foreach(self):
            return self.getTypedRuleContext(D96Parser.Stat_foreachContext,0)


        def stat_break(self):
            return self.getTypedRuleContext(D96Parser.Stat_breakContext,0)


        def stat_continue(self):
            return self.getTypedRuleContext(D96Parser.Stat_continueContext,0)


        def stat_return(self):
            return self.getTypedRuleContext(D96Parser.Stat_returnContext,0)


        def stat_method_ins(self):
            return self.getTypedRuleContext(D96Parser.Stat_method_insContext,0)


        def stat_method_sta(self):
            return self.getTypedRuleContext(D96Parser.Stat_method_staContext,0)


        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = D96Parser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stat)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.stat_var_con()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.stat_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.stat_if()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.stat_foreach()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 310
                self.stat_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 311
                self.stat_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 312
                self.stat_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 313
                self.stat_method_ins()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 314
                self.stat_method_sta()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 315
                self.stat_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_var_conContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def stat_var_con1(self):
            return self.getTypedRuleContext(D96Parser.Stat_var_con1Context,0)


        def stat_var_con2(self):
            return self.getTypedRuleContext(D96Parser.Stat_var_con2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_var_con

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_var_con" ):
                return visitor.visitStat_var_con(self)
            else:
                return visitor.visitChildren(self)




    def stat_var_con(self):

        localctx = D96Parser.Stat_var_conContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stat_var_con)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 319
                self.stat_var_con1()
                pass

            elif la_ == 2:
                self.state = 320
                self.stat_var_con2()
                pass


            self.state = 323
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_var_con1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_id_ins(self):
            return self.getTypedRuleContext(D96Parser.List_id_insContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_var_con1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_var_con1" ):
                return visitor.visitStat_var_con1(self)
            else:
                return visitor.visitChildren(self)




    def stat_var_con1(self):

        localctx = D96Parser.Stat_var_con1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stat_var_con1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.list_id_ins()
            self.state = 326
            self.match(D96Parser.COLON)
            self.state = 327
            self.mptype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_var_con2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def stat_var_con2(self):
            return self.getTypedRuleContext(D96Parser.Stat_var_con2Context,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def ASS(self):
            return self.getToken(D96Parser.ASS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stat_var_con2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_var_con2" ):
                return visitor.visitStat_var_con2(self)
            else:
                return visitor.visitChildren(self)




    def stat_var_con2(self):

        localctx = D96Parser.Stat_var_con2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stat_var_con2)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(D96Parser.ID)
                self.state = 330
                self.match(D96Parser.COMMA)
                self.state = 331
                self.stat_var_con2()
                self.state = 332
                self.match(D96Parser.COMMA)
                self.state = 333
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.match(D96Parser.ID)
                self.state = 336
                self.match(D96Parser.COLON)
                self.state = 337
                self.mptype()
                self.state = 338
                self.match(D96Parser.ASS)
                self.state = 339
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_id_insContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_id_ins(self):
            return self.getTypedRuleContext(D96Parser.List_id_insContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_id_ins

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_id_ins" ):
                return visitor.visitList_id_ins(self)
            else:
                return visitor.visitChildren(self)




    def list_id_ins(self):

        localctx = D96Parser.List_id_insContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_list_id_ins)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(D96Parser.ID)
                self.state = 344
                self.match(D96Parser.COMMA)
                self.state = 345
                self.list_id_ins()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_assign_lhs(self):
            return self.getTypedRuleContext(D96Parser.Stat_assign_lhsContext,0)


        def ASS(self):
            return self.getToken(D96Parser.ASS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stat_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_assign" ):
                return visitor.visitStat_assign(self)
            else:
                return visitor.visitChildren(self)




    def stat_assign(self):

        localctx = D96Parser.Stat_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stat_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.stat_assign_lhs()
            self.state = 350
            self.match(D96Parser.ASS)
            self.state = 351
            self.expr()
            self.state = 352
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_assign_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mpid(self):
            return self.getTypedRuleContext(D96Parser.MpidContext,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_assign_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_assign_lhs" ):
                return visitor.visitStat_assign_lhs(self)
            else:
                return visitor.visitChildren(self)




    def stat_assign_lhs(self):

        localctx = D96Parser.Stat_assign_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_stat_assign_lhs)
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.mpid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.expr7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def part_if(self):
            return self.getTypedRuleContext(D96Parser.Part_ifContext,0)


        def list_else(self):
            return self.getTypedRuleContext(D96Parser.List_elseContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_if" ):
                return visitor.visitStat_if(self)
            else:
                return visitor.visitChildren(self)




    def stat_if(self):

        localctx = D96Parser.Stat_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stat_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.part_if()
            self.state = 359
            self.list_else()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Part_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_part_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPart_if" ):
                return visitor.visitPart_if(self)
            else:
                return visitor.visitChildren(self)




    def part_if(self):

        localctx = D96Parser.Part_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_part_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(D96Parser.IF)
            self.state = 362
            self.match(D96Parser.LB)
            self.state = 363
            self.expr()
            self.state = 364
            self.match(D96Parser.RB)
            self.state = 365
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif(self):
            return self.getTypedRuleContext(D96Parser.ElseifContext,0)


        def list_else(self):
            return self.getTypedRuleContext(D96Parser.List_elseContext,0)


        def part_else(self):
            return self.getTypedRuleContext(D96Parser.Part_elseContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else" ):
                return visitor.visitList_else(self)
            else:
                return visitor.visitChildren(self)




    def list_else(self):

        localctx = D96Parser.List_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_list_else)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.elseif()
                self.state = 368
                self.list_else()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.part_else()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif" ):
                return visitor.visitElseif(self)
            else:
                return visitor.visitChildren(self)




    def elseif(self):

        localctx = D96Parser.ElseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elseif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(D96Parser.ELSEIF)
            self.state = 375
            self.match(D96Parser.LB)
            self.state = 376
            self.expr()
            self.state = 377
            self.match(D96Parser.RB)
            self.state = 378
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Part_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_part_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPart_else" ):
                return visitor.visitPart_else(self)
            else:
                return visitor.visitChildren(self)




    def part_else(self):

        localctx = D96Parser.Part_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_part_else)
        try:
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.match(D96Parser.ELSE)
                self.state = 381
                self.stat_block()
                pass
            elif token in [D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.TRUE, D96Parser.IF, D96Parser.FALSE, D96Parser.VAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.VAR, D96Parser.RETURN, D96Parser.SELF, D96Parser.ID, D96Parser.ID_STATIC, D96Parser.LB, D96Parser.LP, D96Parser.RP, D96Parser.LIT_INT, D96Parser.LIT_FLOAT, D96Parser.LIT_STRING]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_foreachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def mpid(self):
            return self.getTypedRuleContext(D96Parser.MpidContext,0)


        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DDOT(self):
            return self.getToken(D96Parser.DDOT, 0)

        def by_expr(self):
            return self.getTypedRuleContext(D96Parser.By_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stat_block(self):
            return self.getTypedRuleContext(D96Parser.Stat_blockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_foreach

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_foreach" ):
                return visitor.visitStat_foreach(self)
            else:
                return visitor.visitChildren(self)




    def stat_foreach(self):

        localctx = D96Parser.Stat_foreachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stat_foreach)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(D96Parser.FOREACH)
            self.state = 386
            self.match(D96Parser.LB)
            self.state = 387
            self.mpid()
            self.state = 388
            self.match(D96Parser.IN)
            self.state = 389
            self.expr()
            self.state = 390
            self.match(D96Parser.DDOT)
            self.state = 391
            self.expr()
            self.state = 392
            self.by_expr()
            self.state = 393
            self.match(D96Parser.RB)
            self.state = 394
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class By_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_by_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBy_expr" ):
                return visitor.visitBy_expr(self)
            else:
                return visitor.visitChildren(self)




    def by_expr(self):

        localctx = D96Parser.By_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_by_expr)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(D96Parser.BY)
                self.state = 397
                self.expr()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stat_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_break" ):
                return visitor.visitStat_break(self)
            else:
                return visitor.visitChildren(self)




    def stat_break(self):

        localctx = D96Parser.Stat_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stat_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(D96Parser.BREAK)
            self.state = 402
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stat_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_continue" ):
                return visitor.visitStat_continue(self)
            else:
                return visitor.visitChildren(self)




    def stat_continue(self):

        localctx = D96Parser.Stat_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stat_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(D96Parser.CONTINUE)
            self.state = 405
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_return" ):
                return visitor.visitStat_return(self)
            else:
                return visitor.visitChildren(self)




    def stat_return(self):

        localctx = D96Parser.Stat_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stat_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(D96Parser.RETURN)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.EXCL) | (1 << D96Parser.MINUS) | (1 << D96Parser.LB) | (1 << D96Parser.LIT_INT) | (1 << D96Parser.LIT_FLOAT) | (1 << D96Parser.LIT_STRING))) != 0):
                self.state = 408
                self.expr()


            self.state = 411
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_method_staContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DCOLON(self):
            return self.getToken(D96Parser.DCOLON, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_method_sta

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_method_sta" ):
                return visitor.visitStat_method_sta(self)
            else:
                return visitor.visitChildren(self)




    def stat_method_sta(self):

        localctx = D96Parser.Stat_method_staContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stat_method_sta)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(D96Parser.ID)
            self.state = 414
            self.match(D96Parser.DCOLON)
            self.state = 415
            self.match(D96Parser.ID_STATIC)
            self.state = 416
            self.match(D96Parser.LB)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.EXCL) | (1 << D96Parser.MINUS) | (1 << D96Parser.LB) | (1 << D96Parser.LIT_INT) | (1 << D96Parser.LIT_FLOAT) | (1 << D96Parser.LIT_STRING))) != 0):
                self.state = 417
                self.list_expr()


            self.state = 420
            self.match(D96Parser.RB)
            self.state = 421
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_method_insContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stat_method_ins

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_method_ins" ):
                return visitor.visitStat_method_ins(self)
            else:
                return visitor.visitChildren(self)




    def stat_method_ins(self):

        localctx = D96Parser.Stat_method_insContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stat_method_ins)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.expr8(0)
            self.state = 424
            self.match(D96Parser.DOT)
            self.state = 425
            self.match(D96Parser.ID)
            self.state = 426
            self.match(D96Parser.LB)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.EXCL) | (1 << D96Parser.MINUS) | (1 << D96Parser.LB) | (1 << D96Parser.LIT_INT) | (1 << D96Parser.LIT_FLOAT) | (1 << D96Parser.LIT_STRING))) != 0):
                self.state = 427
                self.list_expr()


            self.state = 430
            self.match(D96Parser.RB)
            self.state = 431
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def block_body(self):
            return self.getTypedRuleContext(D96Parser.Block_bodyContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stat_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_block" ):
                return visitor.visitStat_block(self)
            else:
                return visitor.visitChildren(self)




    def stat_block(self):

        localctx = D96Parser.Stat_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stat_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(D96Parser.LP)
            self.state = 434
            self.block_body()
            self.state = 435
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_stat(self):
            return self.getTypedRuleContext(D96Parser.List_statContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_block_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_body" ):
                return visitor.visitBlock_body(self)
            else:
                return visitor.visitChildren(self)




    def block_body(self):

        localctx = D96Parser.Block_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_block_body)
        try:
            self.state = 439
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BREAK, D96Parser.FOREACH, D96Parser.CONTINUE, D96Parser.TRUE, D96Parser.IF, D96Parser.FALSE, D96Parser.VAL, D96Parser.NEW, D96Parser.ARRAY, D96Parser.VAR, D96Parser.RETURN, D96Parser.SELF, D96Parser.ID, D96Parser.ID_STATIC, D96Parser.LB, D96Parser.LP, D96Parser.LIT_INT, D96Parser.LIT_FLOAT, D96Parser.LIT_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.list_stat()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(D96Parser.StatContext,0)


        def list_stat(self):
            return self.getTypedRuleContext(D96Parser.List_statContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stat" ):
                return visitor.visitList_stat(self)
            else:
                return visitor.visitChildren(self)




    def list_stat(self):

        localctx = D96Parser.List_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_list_stat)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.stat()
                self.state = 442
                self.list_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def op_string(self):
            return self.getTypedRuleContext(D96Parser.Op_stringContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.expr1()
                self.state = 448
                self.op_string()
                self.state = 449
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def op_rel(self):
            return self.getTypedRuleContext(D96Parser.Op_relContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr1)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.expr2(0)
                self.state = 455
                self.op_rel()
                self.state = 456
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def op_log2(self):
            return self.getTypedRuleContext(D96Parser.Op_log2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 464
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 465
                    self.op_log2()
                    self.state = 466
                    self.expr3(0) 
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def op_add(self):
            return self.getTypedRuleContext(D96Parser.Op_addContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 476
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 477
                    self.op_add()
                    self.state = 478
                    self.expr4(0) 
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def op_mul(self):
            return self.getTypedRuleContext(D96Parser.Op_mulContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 494
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 488
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 489
                    self.op_mul()
                    self.state = 490
                    self.expr5() 
                self.state = 496
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_log1(self):
            return self.getTypedRuleContext(D96Parser.Op_log1Context,0)


        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_expr5)
        try:
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.EXCL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.op_log1()
                self.state = 498
                self.expr5()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.ID_STATIC, D96Parser.MINUS, D96Parser.LB, D96Parser.LIT_INT, D96Parser.LIT_FLOAT, D96Parser.LIT_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr6)
        try:
            self.state = 506
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.match(D96Parser.MINUS)
                self.state = 504
                self.expr6()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.NEW, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.ID_STATIC, D96Parser.LB, D96Parser.LIT_INT, D96Parser.LIT_FLOAT, D96Parser.LIT_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = D96Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_expr7)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.expr8(0)
                self.state = 509
                self.match(D96Parser.LS)
                self.state = 510
                self.expr()
                self.state = 511
                self.match(D96Parser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def LS(self):
            return self.getToken(D96Parser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RS(self):
            return self.getToken(D96Parser.RS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.expr9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 526
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 519
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 520
                    self.match(D96Parser.LS)
                    self.state = 521
                    self.expr()
                    self.state = 522
                    self.match(D96Parser.RS) 
                self.state = 528
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.expr10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 545
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 543
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 532
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 533
                        self.match(D96Parser.DOT)
                        self.state = 534
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 535
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 536
                        self.match(D96Parser.DOT)
                        self.state = 537
                        self.match(D96Parser.ID)
                        self.state = 538
                        self.match(D96Parser.LB)
                        self.state = 540
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.EXCL) | (1 << D96Parser.MINUS) | (1 << D96Parser.LB) | (1 << D96Parser.LIT_INT) | (1 << D96Parser.LIT_FLOAT) | (1 << D96Parser.LIT_STRING))) != 0):
                            self.state = 539
                            self.list_expr()


                        self.state = 542
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 547
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DCOLON(self):
            return self.getToken(D96Parser.DCOLON, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.match(D96Parser.ID)
                self.state = 549
                self.match(D96Parser.DCOLON)
                self.state = 550
                self.match(D96Parser.ID_STATIC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.match(D96Parser.ID)
                self.state = 552
                self.match(D96Parser.DCOLON)
                self.state = 553
                self.match(D96Parser.ID_STATIC)
                self.state = 554
                self.match(D96Parser.LB)
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.EXCL) | (1 << D96Parser.MINUS) | (1 << D96Parser.LB) | (1 << D96Parser.LIT_INT) | (1 << D96Parser.LIT_FLOAT) | (1 << D96Parser.LIT_STRING))) != 0):
                    self.state = 555
                    self.list_expr()


                self.state = 558
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 559
                self.expr11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def factor(self):
            return self.getTypedRuleContext(D96Parser.FactorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_expr11)
        self._la = 0 # Token type
        try:
            self.state = 570
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.match(D96Parser.NEW)
                self.state = 563
                self.match(D96Parser.ID)
                self.state = 564
                self.match(D96Parser.LB)
                self.state = 566
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.TRUE) | (1 << D96Parser.FALSE) | (1 << D96Parser.NEW) | (1 << D96Parser.ARRAY) | (1 << D96Parser.SELF) | (1 << D96Parser.ID) | (1 << D96Parser.ID_STATIC) | (1 << D96Parser.EXCL) | (1 << D96Parser.MINUS) | (1 << D96Parser.LB) | (1 << D96Parser.LIT_INT) | (1 << D96Parser.LIT_FLOAT) | (1 << D96Parser.LIT_STRING))) != 0):
                    self.state = 565
                    self.list_expr()


                self.state = 568
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.SELF, D96Parser.ID, D96Parser.ID_STATIC, D96Parser.LB, D96Parser.LIT_INT, D96Parser.LIT_FLOAT, D96Parser.LIT_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mpid(self):
            return self.getTypedRuleContext(D96Parser.MpidContext,0)


        def lit(self):
            return self.getTypedRuleContext(D96Parser.LitContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = D96Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_factor)
        try:
            self.state = 579
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.ID_STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.mpid()
                pass
            elif token in [D96Parser.TRUE, D96Parser.FALSE, D96Parser.ARRAY, D96Parser.LIT_INT, D96Parser.LIT_FLOAT, D96Parser.LIT_STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 573
                self.lit()
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 574
                self.match(D96Parser.LB)
                self.state = 575
                self.expr()
                self.state = 576
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 578
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIT_INT(self):
            return self.getToken(D96Parser.LIT_INT, 0)

        def LIT_STRING(self):
            return self.getToken(D96Parser.LIT_STRING, 0)

        def LIT_FLOAT(self):
            return self.getToken(D96Parser.LIT_FLOAT, 0)

        def lit_boolean(self):
            return self.getTypedRuleContext(D96Parser.Lit_booleanContext,0)


        def lit_indexed_arr(self):
            return self.getTypedRuleContext(D96Parser.Lit_indexed_arrContext,0)


        def lit_mul_arr(self):
            return self.getTypedRuleContext(D96Parser.Lit_mul_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = D96Parser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_lit)
        try:
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(D96Parser.LIT_INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.match(D96Parser.LIT_STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
                self.match(D96Parser.LIT_FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 584
                self.lit_boolean()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 585
                self.lit_indexed_arr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 586
                self.lit_mul_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUA_DOT(self):
            return self.getToken(D96Parser.EQUA_DOT, 0)

        def PLUS_DOT(self):
            return self.getToken(D96Parser.PLUS_DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_string" ):
                return visitor.visitOp_string(self)
            else:
                return visitor.visitChildren(self)




    def op_string(self):

        localctx = D96Parser.Op_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_op_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            _la = self._input.LA(1)
            if not(_la==D96Parser.EQUA_DOT or _la==D96Parser.PLUS_DOT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_relContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUA(self):
            return self.getToken(D96Parser.EQUA, 0)

        def DIF(self):
            return self.getToken(D96Parser.DIF, 0)

        def LESS(self):
            return self.getToken(D96Parser.LESS, 0)

        def MOREE(self):
            return self.getToken(D96Parser.MOREE, 0)

        def LESS_EQUA(self):
            return self.getToken(D96Parser.LESS_EQUA, 0)

        def MORE_EQUA(self):
            return self.getToken(D96Parser.MORE_EQUA, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_rel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_rel" ):
                return visitor.visitOp_rel(self)
            else:
                return visitor.visitChildren(self)




    def op_rel(self):

        localctx = D96Parser.Op_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_op_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.DIF) | (1 << D96Parser.MOREE) | (1 << D96Parser.LESS_EQUA) | (1 << D96Parser.EQUA) | (1 << D96Parser.LESS) | (1 << D96Parser.MORE_EQUA))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_log2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_log2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_log2" ):
                return visitor.visitOp_log2(self)
            else:
                return visitor.visitChildren(self)




    def op_log2(self):

        localctx = D96Parser.Op_log2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_op_log2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            _la = self._input.LA(1)
            if not(_la==D96Parser.AND or _la==D96Parser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(D96Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(D96Parser.MINUS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_add

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_add" ):
                return visitor.visitOp_add(self)
            else:
                return visitor.visitChildren(self)




    def op_add(self):

        localctx = D96Parser.Op_addContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_op_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            _la = self._input.LA(1)
            if not(_la==D96Parser.PLUS or _la==D96Parser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_mulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def PERCENT(self):
            return self.getToken(D96Parser.PERCENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_mul

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_mul" ):
                return visitor.visitOp_mul(self)
            else:
                return visitor.visitChildren(self)




    def op_mul(self):

        localctx = D96Parser.Op_mulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_op_mul)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.PERCENT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_log1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCL(self):
            return self.getToken(D96Parser.EXCL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_log1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_log1" ):
                return visitor.visitOp_log1(self)
            else:
                return visitor.visitChildren(self)




    def op_log1(self):

        localctx = D96Parser.Op_log1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_op_log1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(D96Parser.EXCL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_objContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_op_obj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_obj" ):
                return visitor.visitOp_obj(self)
            else:
                return visitor.visitChildren(self)




    def op_obj(self):

        localctx = D96Parser.Op_objContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_op_obj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(D96Parser.NEW)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MpidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ID_STATIC(self):
            return self.getToken(D96Parser.ID_STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mpid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMpid" ):
                return visitor.visitMpid(self)
            else:
                return visitor.visitChildren(self)




    def mpid(self):

        localctx = D96Parser.MpidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_mpid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.ID_STATIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_booleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(D96Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(D96Parser.FALSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lit_boolean

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_boolean" ):
                return visitor.visitLit_boolean(self)
            else:
                return visitor.visitChildren(self)




    def lit_boolean(self):

        localctx = D96Parser.Lit_booleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_lit_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            _la = self._input.LA(1)
            if not(_la==D96Parser.TRUE or _la==D96Parser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_indexed_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lit_indexed_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_indexed_arr" ):
                return visitor.visitLit_indexed_arr(self)
            else:
                return visitor.visitChildren(self)




    def lit_indexed_arr(self):

        localctx = D96Parser.Lit_indexed_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_lit_indexed_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(D96Parser.ARRAY)
            self.state = 608
            self.match(D96Parser.LB)
            self.state = 609
            self.list_expr()
            self.state = 610
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_mul_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def mul_arr_elements(self):
            return self.getTypedRuleContext(D96Parser.Mul_arr_elementsContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lit_mul_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_mul_arr" ):
                return visitor.visitLit_mul_arr(self)
            else:
                return visitor.visitChildren(self)




    def lit_mul_arr(self):

        localctx = D96Parser.Lit_mul_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_lit_mul_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.match(D96Parser.ARRAY)
            self.state = 613
            self.match(D96Parser.LB)
            self.state = 614
            self.mul_arr_elements()
            self.state = 615
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_arr_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mul_arr_element(self):
            return self.getTypedRuleContext(D96Parser.Mul_arr_elementContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def mul_arr_elements(self):
            return self.getTypedRuleContext(D96Parser.Mul_arr_elementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mul_arr_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_arr_elements" ):
                return visitor.visitMul_arr_elements(self)
            else:
                return visitor.visitChildren(self)




    def mul_arr_elements(self):

        localctx = D96Parser.Mul_arr_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_mul_arr_elements)
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self.mul_arr_element()
                self.state = 618
                self.match(D96Parser.COMMA)
                self.state = 619
                self.mul_arr_elements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self.mul_arr_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_arr_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit_mul_arr(self):
            return self.getTypedRuleContext(D96Parser.Lit_mul_arrContext,0)


        def lit_indexed_arr(self):
            return self.getTypedRuleContext(D96Parser.Lit_indexed_arrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_mul_arr_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_arr_element" ):
                return visitor.visitMul_arr_element(self)
            else:
                return visitor.visitChildren(self)




    def mul_arr_element(self):

        localctx = D96Parser.Mul_arr_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_mul_arr_element)
        try:
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.lit_mul_arr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.lit_indexed_arr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[51] = self.expr2_sempred
        self._predicates[52] = self.expr3_sempred
        self._predicates[53] = self.expr4_sempred
        self._predicates[57] = self.expr8_sempred
        self._predicates[58] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




