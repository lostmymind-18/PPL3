import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program1(self):
        """sao ko duoc"""
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input,expect,301))
        
    def test_simple_program2(self):
        """sao ko duoc"""
        input = """Class Rectangle : Shape {}"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_program3(self):
        """xxx"""
        input="""Class Rectangle {
            Var length: Int;
        }"""
        expect="Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_simple_program4(self):
        """xxx"""
        input="""Class Rectangle {
            Var x: Int = 10;
        }"""
        expect="Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_simple_program5(self):
        """xxx"""
        input="""Class Rectangle {
            Val $x: Int = 10;
        }"""
        expect="Program([ClassDecl(Id(Rectangle),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(10)))])])"
        self.assertTrue(TestAST.test(input,expect,305))
