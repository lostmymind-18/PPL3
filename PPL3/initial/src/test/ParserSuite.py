import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_class_declare1(self):
        """Simple program: int main() {} """
        input = r"""
Class Rectangle{
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_class_declare2(self):
        """Simple program: int main() {} """
        input = r"""
Class Rectangle:Shape{
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_class_declare3(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape:Rectangle{
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,203))
        
    def test_class_declare4(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {}
    Constructor(){}
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,204))
        
    def test_class_declare5(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape() {}
    Constructor(){}
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,205))
        
    def test_class_declare6(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0X123_AFE_343;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG = "123","abc";
    $getNumOfShape($numOfShape,length:STRING; width,abc:INT) {}
    Constructor($abc:INT;Abc:FLOAT){}
    Destructor(){}
}

Class Shape {
    Val $numOfShape: Int = 0X123_AFE_343;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG = "123","abc";
    $getNumOfShape($numOfShape,length:STRING; width,abc:INT) {}
    Constructor($abc:INT;Abc:FLOAT){}
    Destructor(){}
}

Class Shape {
    Val $numOfShape: Int = 0X123_AFE_343;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG = "123","abc";
    $getNumOfShape($numOfShape,length:STRING; width,abc:INT) {}
    Constructor($abc:INT;Abc:FLOAT){}
    Destructor(){}
}
"""
        expect = r"Error on line 6 col 19: $numOfShape"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_class_declare7(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0X123_AFE_343;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length: STrInG= "123";
    $getNumOfShape(numOfShape,length:STRING; width,abc:INT) {}
    Constructor(abc:INT;Abc:FLOAT){}
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,207))
        
    def test_class_declare8(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0X123_AFE_343;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var STrInG, FLOAT = "123";
    $getNumOfShape($numOfShape,length:STRING; width,abc:INT) {}
    Constructor($abc:INT;Abc:FLOAT){}
    Destructor(){}
}
"""
        expect = r"Error on line 5 col 8: STrInG"
        self.assertTrue(TestParser.test(input,expect,208))
        
    def test_class_declare9(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0X123_AFE_343;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var x: INT = 123,456;
    $getNumOfShape($numOfShape,length:STRING; width,abc:INT) {}
    Constructor($abc:INT;Abc:FLOAT){}
    Destructor(abc:INT){}
}
"""
        expect = r"Error on line 5 col 20: ,"
        self.assertTrue(TestParser.test(input,expect,209))
        
    def test_class_declare10(self):
        """Simple program: int main() {} """
        input = r"""
Class Shape {
    Val $numOfShape: Int;
    Val immutableAttribute: FLOAT;
    Var x,y: FLOAT = 18.E-3;
    $getNumOfShape($numOfShape,length:STRING; width,abc:INT) {}
    Constructor($abc:INT;Abc:FLOAT){}
    Destructor(){}
}
"""
        expect = r"Error on line 5 col 27: ;"
        self.assertTrue(TestParser.test(input,expect,210))        
                         
                         
                                                        
    def test_stmt_assn1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = 5;
        y = 6;
        z = 7;
    }
    Constructor(x,y,z:INT){
        Self.x = x;
        Self.y = y;
        Self.z = z;
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,211))
        
    def test_stmt_assn2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = 5*3/4+7*2-($i-8);
        y = $abc[4/3+((5-i)+3.4E-5)];
        z = 7;
    }
    Constructor(x,y,z:INT){
        Self.x = x/x*x;
        Self.y = CA__.aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,212))  
        
    def test_stmt_assn3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = abc::$a($a,b,5,"xyz");
        z = abc.ynx($a,b,5,"xyz");
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,213))
        
    def test_stmt_assn4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = !((abc::$a($a,b,5,"xyz") +. "abc") ==. "abc");
        z = !!!!!!!(True && False);
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.$aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"Error on line 13 col 22: $aaabc___"
        self.assertTrue(TestParser.test(input,expect,214))
        
    def test_stmt_assn5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = (34.5E-301 + 5) - 9/2*7;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
    }
    Constructor(x,y,z:INT){
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,215))
        
    def test_stmt_assn6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = !((abc::$a($a,b,5,"xyz") +. "abc") ==. "abc");
        z = "abc" +. "xyz" +. "8a";
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.$aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"Error on line 9 col 27: +."
        self.assertTrue(TestParser.test(input,expect,216))
        
    def test_stmt_assn7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = !((abc::$a($abc[],b,5,"xyz") +. "abc") ==. "abc");
        z = "abc" +. "xyz";
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.$aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"Error on line 8 col 28: ]"
        self.assertTrue(TestParser.test(input,expect,217))
        
    def test_stmt_assn8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,218))
    
    def test_stmt_assn9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,219))
        
    def test_stmt_assn10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_stmt_if1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If()
        {
             x = 5+3;
        }
    }
}
"""
        expect = r"Error on line 9 col 11: )"
        self.assertTrue(TestParser.test(input,expect,221))
        
    def test_stmt_if2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
        }
        Elseif()
        {
             y = $a;
        }
    }
}
"""
        expect = r"Error on line 13 col 15: )"
        self.assertTrue(TestParser.test(input,expect,222))
        
    def test_stmt_if3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
        }
        Elseif(True)
        {
             y = $a;
        }
        Elseif(False)
    }
}
"""
        expect = r"Error on line 18 col 4: }"
        self.assertTrue(TestParser.test(input,expect,223))
        
    def test_stmt_if4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
        }
        Elseif(True)
        {
             y = $a;
        }
        Elseif(False)
        {
        }
        Else{}
        Else{}
    }
}
"""
        expect = r"Error on line 21 col 8: Else"
        self.assertTrue(TestParser.test(input,expect,224))
        
    def test_stmt_if5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
        }
        If($a > 5)
        {
             x = 5+3;
        }
        If($a > 5)
        {
             x = 5+3;
        }
        If($a > 5)
        {
             x = 5+3;
        }
        If($a > 5)
        {
             x = 5+3;
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,225))
        
    def test_stmt_if6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
             If(True)
             {
                 If(False)
                 {
                      x = 7;
                 }         
             }
             
             Else
             {
                  y = 5;
             }
        }
        Else{
            z = 8;
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,226))
        
    def test_stmt_if7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
             If(True)
             {
                 If(False)
                 {
                      x = 7;
                 }         
             }
             
             Else
             {
                  y = 5;
                  Elseif(5>3){}
             }
        }
        Else{
            z = 8;
        }
    }
}
"""
        expect = r"Error on line 22 col 18: Elseif"
        self.assertTrue(TestParser.test(input,expect,227))
        
    def test_stmt_if8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5){}
        Else{
            If(a){
                If($a){}
                Else{}
            }
            Elseif(a){
                If($a){}
                Else{}
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,228))
        
    def test_stmt_if9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
            If($a>5)
            {
                If($a>5)
                {
                    If($a>5){}
                }
            }
        }
        Else
        {
            If($a > 5)
            {
                If($a>5)
                {
                    If($a>5)
                    {
                    If($a>5){}
                    }
                }
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,229))
        
    def test_stmt_if10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
            If($a>5)
            {
                If($a>5)
                {
                    If($a>5){}
                }
            }
        }
        Else
        {
            If($a > 5)
            {
                If($a>5)
                {
                    If($a>5)
                    {
                    If($a>5){}
                    }
                }
                
            }
            Else
            {
                If($a > 5)
                {
                    If($a>5)
                    {
                        If($a>5)
                        {
                            If($a>5){}
                         }
                    }
                }
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_stmt_foreach1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(i In 1 .. 100 By 2){
            Out.printInt(i);
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,231))
        
    def test_stmt_foreach2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 1 .. 100){
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,232))
        
    def test_stmt_foreach3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Out.printInt(arr[x]);
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,233))
        
    def test_stmt_foreach4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,234))
        
    def test_stmt_foreach5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,235))
        
    def test_stmt_foreach6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,236))
        
    def test_stmt_foreach7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By $a){}
        FOREACH(X IN 8*3.4e-56 .. 100 By a){}
        FOREACH(X IN 8*3.4e-56 .. 100 By abc.abc){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 99){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,237))
        
    def test_stmt_foreach8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By $a){}
        FOREACH(X IN 8*3.4e-56 .. By a){}
        FOREACH(X IN 8*3.4e-56 .. 100 By abc.abc){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 99){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
    }
}
"""
        expect = r"Error on line 10 col 34: By"
        self.assertTrue(TestParser.test(input,expect,238))
        
    def test_stmt_foreach9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By $a){}
        FOREACH(X IN .. 100 By a){}
        FOREACH(X IN 8*3.4e-56 .. 100 By abc.abc){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 99){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
    }
}
"""
        expect = r"Error on line 10 col 21: .."
        self.assertTrue(TestParser.test(input,expect,239))        
       
    def test_stmt_foreach10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By $a){
            FOREACH(X IN 8*3.4e-56 .. 100 By $a){}
            FOREACH(X IN 4 .. 100 By a){}
            FOREACH(X IN 8*3.4e-56 .. 100 By abc.abc){}
            FOREACH(X IN 8*3.4e-56 .. 100 By 99){}
            FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
        }
        FOREACH(X IN 4 .. 100 By a){}
        FOREACH(X IN 8*3.4e-56 .. 100 By abc.abc){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 99){}
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_stmt_break_continue1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
                Break;
            }
            Break;
        }
        Continue;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,241))
        
    def test_stmt_break_continue2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
                Break;
            }
            Continue;
        }
        BREAK;
        CONTinUE;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,242))  
                                                             
    def test_stmt_break_continue3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Break;
        Continue;
        BREAK;
        CONTINUE;
        COnTiNue;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,243))
    
    def test_stmt_break_continue4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
             Break;
        }
        Elseif(True)
        {
             y = $a;
             Continue;
        }
        Break;
        Continue;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,244))
        
    def test_stmt_break_continue5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
             If(True)
             {
                 If(False)
                 {
                      x = 7;
                      Break;
                 }         
                 Continue;
             }
             
             Else
             {
                  y = 5;
                  Break;
                  Continue;
             }
        }
        Else{
            z = 8;
            Break;
            Continue;
        }
        Continue;
        Break;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,245))
        
    def test_stmt_break_continue6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            If(i > 5) 
            {
                Continue;
            }
            Break;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Break;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Continue;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Break;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,246))
        
    def test_stmt_break_continue7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
            If($a>5)
            {
                If($a>5)
                {
                    If($a>5){}
                }
            }
        }
        Else
        {
            If($a > 5)
            {
                If($a>5)
                {
                    If($a>5)
                    {
                        If($a>5){
                            Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
                        }
                    }
                }
                Break;
            }
            Else
            {
                If($a > 5)
                {
                    If($a>5)
                    {
                        If($a>5)
                        {
                            If($a>5){}
                         }
                    }
                }
                Continue;
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,247))
        
    def test_stmt_break_continue8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        If(True){}
                        Elseif(True)
                        {
                             y = $a;
                             Break;
                             Continue;
                        }
                        Elseif(False){
                             Break;
                             Continue;
                        }
                        Else{
                             Break;
                             Continue;
                        }
                    }
                }
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,248))
        
    def test_stmt_break_continue9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Out.printInt(arr[x]);
        
            If($a > 5)
            {
                x = 5+3;
                Break;
            }
            Elseif(True)
            {
                 y = $a;
                 Continue;
                 Break;
            }
            Elseif(False){}
            Break;
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,249))
        
    def test_stmt_break_continue10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By $a){
            If($a > 5)
            {
                x = 5+3;
                Break;
            }
            If($a > 5)
            {
                x = 5+3;
                Break;
            }
            If($a > 5)
            {
                x = 5+3;
                Break;
            }
            If($a > 5)
            {
                x = 5+3;
                Break;
            }
            If($a > 5)
            {
                x = 5+3;
                Break;
            }
        }

    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_stmt_return1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,251))
        
    def test_stmt_return2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        RETURn;
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return;
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return;
    }        
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,252)) 
        
    def test_stmt_return3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        RETURn 5+8*3;
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return 8*3+7;
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return 3-1+5/2;
    }        
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,253)) 
        
    def test_stmt_return4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        RETURn 34.5E-301;
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return !!!!!!!(True && False);
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return ("abc" +. "cdb") ==. "xyz";
    }        
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,254)) 
        
    def test_stmt_return5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        RETURn -----(((5)));
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return !!!!!!!(True && False);
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return "@@@@@@";
    }        
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,255)) 
        
    def test_stmt_return6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        RETURn index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")];
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")];
    }
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return "@@@@@@";
    }        
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,256)) 
        
    def test_stmt_return7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Out.printInt(arr[x]);
        
            If($a > 5)
            {
                x = 5+3;
                Return x;
                Break;
            }
            Elseif(True)
            {
                 y = $a;
                 Continue;
                 Break;
                 Return x;
            }
            Elseif(False){}
            Break;
            Return x;
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,257)) 
        
    def test_stmt_return8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            If(i > 5) 
            {
                Continue;
            }
            Break;
            Return;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Break;
            Return;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Continue;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Break;
            Return;
        }
        FOREACH(X IN 8*3.4e-56 .. 100 By 2.4e-4){
            Return;
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,258)) 
        
    def test_stmt_return9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        Return;
        ReturN;
        RETURN;
        RETurN;
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,259)) 
        
    def test_stmt_return10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Return;
        Continue;
        Return Return xx538__;
    }
}
"""
        expect = r"Error on line 11 col 15: Return"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_stmt_method1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        Shape::$getNumOfShape();
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,261))
        
    def test_stmt_method2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
       Shape::getNumOfShape();
    }
}
"""
        expect = r"Error on line 7 col 14: getNumOfShape"
        self.assertTrue(TestParser.test(input,expect,262)) 
        
    def test_stmt_method3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
       Shape.getNumOfShape();
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,263)) 
        
    def test_stmt_method4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
       Shape.$getNumOfShape();
    }
}
"""
        expect = r"Error on line 7 col 13: $getNumOfShape"
        self.assertTrue(TestParser.test(input,expect,264)) 
        
    def test_stmt_method5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        Shape::$getNumOfShape(4,2,"abc");
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,265)) 
        
    def test_stmt_method6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        Shape::$getNumOfShape(4,2,"abc");
        Shape.getNum(4,2,Shape.getNum(3,5,"abc"));
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,266)) 
        
    def test_stmt_method7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = Shape::$abc()::$xyz();
    }
}
"""
        expect = r"Error on line 7 col 25: ::"
        self.assertTrue(TestParser.test(input,expect,267)) 
        
    def test_stmt_method8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        Self.getNumOfShape();
        Self.getNumOfShape.getNum();
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,268)) 
        
    def test_stmt_method9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        ABC::$getNUm().gadf();
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,269)) 
        
    def test_stmt_method10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        AbC::$GetNum().gasdf(abc.anc()).abc();
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_stmt_block1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{
	}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_stmt_block2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{
		{
			{
			}
		}
	} 
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,272)) 
        
    def test_stmt_block3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
    {
	{
		{
			{
			}
			
		}
	}
	{
		{
			{
			}
		}
	}
    }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,273)) 
        
    def test_stmt_block4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{
		{
			{
			}
			}
		}
	}
	
    }
}
"""
        expect = r"Error on line 16 col 0: }"
        self.assertTrue(TestParser.test(input,expect,274)) 
        
    def test_stmt_block5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
    {
	{
		{
			{
			}
			
		}
	}
	    {
	{
		{
			{
			}
			
		}
	}
	{
		{
			{
			}
		}
	}
    }
	{
		{
			{
			}
		}
	}
    }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,275)) 
        
    def test_stmt_block6(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
    {
	{
		{
			{
			}
			
		}
	}
	    {
	{
		{
			{
			}
			
		}
	}
	{
		{
			{
			
			    {
	{
		{
			{
			}
			
		}
	}
	    {
	{
		{
			{
			}
			
		}
	}
	{
		{
			{
			}
		}
	}
    }
	{
		{
			{
			}
		}
	}
    }
			
			}
		}
	}
    }
	{
		{
			{
			}
		}
	}
    }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,276)) 
        
    def test_stmt_block7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{}{}{}{}{}{}{}{}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,277)) 
        
    def test_stmt_block8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,278)) 
        
    def test_stmt_block9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{}}}}}{}}}}}
    }
}
"""
        expect = r"Error on line 8 col 4: }"
        self.assertTrue(TestParser.test(input,expect,279)) 
        
    def test_stmt_block10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,280))
        
    def test_all1(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = abc::$a($a,b,5,"xyz");
        z = abc.ynx($a,b,5,"xyz");
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
             Break;
        }
        Elseif(True)
        {
             y = $a;
             Continue;
        }
        Break;
        Continue;
                x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,281))
        
    def test_all2(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = abc::$a($a,b,5,"xyz");
        z = abc.ynx($a,b,5,"xyz");
        x = index[index[3][index[3][3]]];
        If($a > 5)
        {
             x = 5+3;
             Break;
        }
        Elseif(True)
        {
             y = $a;
             Continue;
        }
        Break;
        Continue;
                x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.aaabc___;
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,282))
        
    def test_all3(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = abc::$a($a,b,5,"xyz");
        z = abc.ynx($a,b,5,"xyz");
        x = index[index[3][index[3][3]]];
        If($a > 5)
        {
             x = 5+3;
             Break;
        }
        Elseif(True)
        {
             y = $a;
             Continue;
        }
        Break;
        Continue;
                x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Continue;
                    }
                }
            }
        }
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,283))
        
    def test_all4(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,284))
        
    def test_all5(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = abc::$a($a,b,5,"xyz");
        z = abc.ynx($a,b,5,"xyz");
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        If($a > 5)
        {
             x = 5+3;
             Break;
             if(True){}
             Elseif(True)
             {
                  y = $a;
                  Continue;
             }
        }
        Elseif(True)
        {
             y = $a;
             Continue;
        }
        Break;
        Continue;
                x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Continue;
                    }
                }
            }
        }
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"Error on line 16 col 15: ("
        self.assertTrue(TestParser.test(input,expect,285))
        
    def test_all6(self):
        """Assignment stament focus"""
        input = r"""
    Val $numOfShape: Int = 0;
    Val immutableAttribute: FLOAT = 34.5E-301;
    Var length, width: STrInG;
    $getNumOfShape(x,y,z:INT) {
        x = -----(((5)));
        y = abc::$a($a,b,5,"xyz");
        z = abc.ynx($a,b,5,"xyz");
        x = index[index[3][index[3][3]]];
        If($a > 5)
        {
             x = 5+3;
             Break;
        }
        Elseif(True)
        {
             y = $a;
             Continue;
        }
        Break;
        Continue;
                x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Continue;
                    }
                }
            }
        }
    }
    Constructor(x,y,z:INT){
        Self.x = New X($a,b,5,"abc");
        Self.y = CA__.aaabc___;
        Self.z = ("abc" +. "cdb") ==. "xyz";
    }
    Destructor(){}
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,286))
        
    def test_all7(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
        x = index[index[3][index[3][3]]];
        index[index[3][index[3][3]]+Abc::$abc(5+8,"dan")] = 9;
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
        Foreach(x In 8-3/2 .. 100 By 50-10){
            Foreach(x In 8-3/2 .. 100 By 50-10){
                Foreach(x In 8-3/2 .. 100 By 50-10){
                    Foreach(x In 8-3/2 .. 100 By 50-10){
                        Break;
                    }
                }
            }
        }
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,287))
        
    def test_all8(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,288))
        
    def test_all9(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,289))
        
    def test_all10(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,290))
        
    def test_all11(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_all12(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,292))
        
    def test_all13(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,293))
        
    def test_all14(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,294))
        
    def test_all15(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,295))
        
    def test_all16(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,296))
        
    def test_all17(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,297))
        
    def test_all18(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,298))
        
    def test_all19(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{{{{}}}}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,299))
        
    def test_all20(self):
        """Assignment stament focus"""
        input = r"""
Class Shape {
    Val $numOfShape: X = New X(3,$a);
    Val x,y: X = New X(), New X();
    Var length, width: Boolean = True, False;
    $getNumOfShape(x,y,z:INT) {
	{{{{{{{}}}}}}}
    }
}
"""
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,300))
                                                                                        
                                                                                             
                                                

                                                                                        
                                                                     
