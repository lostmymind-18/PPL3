import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier1(self):
        """test instance identifiers"""
        self.assertTrue(TestLexer.test("a_bc","a_bc,<EOF>",101))
    
    def test_identifier2(self):
        """test instance identifiers"""
        self.assertTrue(TestLexer.test("A_5b09c","A_5b09c,<EOF>",102))
        
    def test_identifier3(self):
        """test instance identifiers"""
        self.assertTrue(TestLexer.test("_ABc123","_ABc123,<EOF>",103))
        
    def test_identifier4(self):
        """test instance identifiers"""
        self.assertTrue(TestLexer.test("Rectangle","Rectangle,<EOF>",104))
        
    def test_identifier5(self):
        """test instance identifiers"""
        self.assertTrue(TestLexer.test("_Ab9","_Ab9,<EOF>",105))
        
    def test_identifier6(self):
        """test static identifiers"""
        self.assertTrue(TestLexer.test("$a_bc","$a_bc,<EOF>",106))
    
    def test_identifier7(self):
        """test static identifiers"""
        self.assertTrue(TestLexer.test("$A_5b09c","$A_5b09c,<EOF>",107))
        
    def test_identifier8(self):
        """test static identifiers"""
        self.assertTrue(TestLexer.test("$_ABc123","$_ABc123,<EOF>",108))
        
    def test_identifier9(self):
        """test static identifiers"""
        self.assertTrue(TestLexer.test("$Rectangle","$Rectangle,<EOF>",109))
        
    def test_identifier10(self):
        """test static identifiers"""
        self.assertTrue(TestLexer.test("$_Ab9","$_Ab9,<EOF>",110))
        
    def test_comment1(self):
        """test comment block"""
        self.assertTrue(TestLexer.test("##abcx##","<EOF>",111))  
       
    def test_comment2(self):
        """test comment block"""
        self.assertTrue(TestLexer.test("$a_990bc##abcx##","$a_990bc,<EOF>",112))
            
    def test_comment3(self):
        """test comment block"""
        self.assertTrue(TestLexer.test("abc##abcx\nbabc\babc@@@##def","abc,def,<EOF>",113))
                
    def test_comment4(self):
        """test comment block"""
        self.assertTrue(TestLexer.test("abc##ab\
                                        cx\
                                        ##def","abc,def,<EOF>",114))
     
    def test_comment5(self):
        """test comment block"""
        self.assertTrue(TestLexer.test("$_abc##abcx@@@@@@~~~~~~","$_abc,<EOF>",115))
        
        
        
    def test_string1(self):
        """test string literal"""
        self.assertTrue(TestLexer.test(""" "abc" ""","abc,<EOF>",116))
        
    def test_string2(self):
       
        self.assertTrue(TestLexer.test(""" "a\\\\bc" ""","a\\\\bc,<EOF>",117))
        
    def test_string3(self):
        
        self.assertTrue(TestLexer.test(""" "She's nice" ""","She's nice,<EOF>",118))
        
    def test_string4(self):
        
        self.assertTrue(TestLexer.test(""" "She's ni\\'ce" ""","She's ni\\'ce,<EOF>",119))
        
    def test_string5(self):
        
        self.assertTrue(TestLexer.test(""" "\\b\\f\\r\\n\\t\\'\\\\" ""","\\b\\f\\r\\n\\t\\'\\\\,<EOF>",120))
        
    def test_string6(self):
        
        self.assertTrue(TestLexer.test(""" "abc'\"@@@" ""","abc'\"@@@,<EOF>",121))
        
    def test_string7(self):
        
        self.assertTrue(TestLexer.test(""" "He asked me: '\"Where is John?'\"" ""","He asked me: '\"Where is John?'\",<EOF>",122))
        
    def test_string8(self):
        
        self.assertTrue(TestLexer.test(""" "'\"'\"'\"'\"'\"" ""","'\"'\"'\"'\"'\",<EOF>",123))
        
    def test_string9(self):
        
        self.assertTrue(TestLexer.test(""" "@'\"\\b\\f'\"@>>>>: '\"\\n\\t\\'@" ""","@'\"\\b\\f'\"@>>>>: '\"\\n\\t\\'@,<EOF>",124))
        
    def test_string10(self):
        
        self.assertTrue(TestLexer.test(""" "$$$$@@@@\\fxxxx>>>: ^^ '\"" "abcxyz" ""","$$$$@@@@\\fxxxx>>>: ^^ '\",abcxyz,<EOF>",125))
        
    def test_keyword1(self):
        """Test keyword"""
        self.assertTrue(TestLexer.test("Break Continue If Elseif Else Foreach True False\
                                        Array In Int Float Boolean String Return Null Class\
                                        Val Var Self Constructor Destructor New By",\
"Break,Continue,If,Elseif,Else,Foreach,True,False,\
Array,In,Int,Float,Boolean,String,Return,Null,Class,\
Val,Var,Self,Constructor,Destructor,New,By,<EOF>",126))

    def test_keyword2(self):
        """Test keyword"""
        self.assertTrue(TestLexer.test("BrEaK CONTINUE IF ElSeIf ElSe FOreAcH TRuE FaLSe\
                                        ArRAy IN InT FlOAT BOOleAn StRing RetURn NUlL CLaSS\
                                        VaL VaR SeLF CoNStRUctOr DeStRuCtOr NEw By",\
"BrEaK,CONTINUE,IF,ElSeIf,ElSe,FOreAcH,TRuE,\
FaLSe,ArRAy,IN,InT,FlOAT,BOOleAn,StRing,RetURn,\
NUlL,CLaSS,VaL,VaR,SeLF,CoNStRUctOr,DeStRuCtOr,NEw,By,<EOF>",127))

    def test_operator(self):
        """test operator"""
        
        self.assertTrue(TestLexer.test("+ - * / % ! && || == = != < <= > >= ==. +.\
 . :: New","+,-,*,/,%,!,&&,||,==,=,!=,<,<=,>,>=,==.,+.,.,::,New,<EOF>",128))
 
    def test_seperator(self):
        """test seperator"""
        
        self.assertTrue(TestLexer.test("( ) [ ] . , ; : { } .."\
        ,"(,),[,],.,,,;,:,{,},..,<EOF>",129))
        
    def test_boolean(self):
        """test boolean"""
        
        self.assertTrue(TestLexer.test("False True FALse TRUE",\
        "False,True,FALse,TRUE,<EOF>",130))
    
    def test_integer1(self):
        """test integer octal notation"""
        
        self.assertTrue(TestLexer.test("0123","0123,<EOF>",131))
        
    def test_integer2(self):
        """test integer octal notation"""
        
        self.assertTrue(TestLexer.test("0_1_2_3","0123,<EOF>",132))
        
    def test_integer3(self):
        """test integer octal notation"""
        
        self.assertTrue(TestLexer.test("0_123_456","0123456,<EOF>",133))
        
    def test_integer4(self):
        """test integer octal notation"""
        
        self.assertTrue(TestLexer.test("01_23_45_67","01234567,<EOF>",134))
        
    def test_integer5(self):
        """test integer octal notation"""
        
        self.assertTrue(TestLexer.test("0764_51243_234_468785","076451243234468785,<EOF>",135))
        
    def test_integer6(self):
        """test integer decimal notation"""
        
        self.assertTrue(TestLexer.test("123456","123456,<EOF>",136))
        
    def test_integer7(self):
        """test integer decimal notation"""
        
        self.assertTrue(TestLexer.test("1___","1,<EOF>",137))
        
    def test_integer8(self):
        """test integer decimal notation"""
        
        self.assertTrue(TestLexer.test("1__23__45___6","123456,<EOF>",138))
        
    def test_integer9(self):
        """test integer decimal notation"""
        
        self.assertTrue(TestLexer.test("1___2345___6","123456,<EOF>",139))
        
    def test_integer10(self):
        """test integer decimal notation"""
        
        self.assertTrue(TestLexer.test("100__0000__","1000000,<EOF>",140))
        
    def test_integer11(self):
        """test integer heximal notation"""
        
        self.assertTrue(TestLexer.test("0XABCDEF","0XABCDEF,<EOF>",141))
        
    def test_integer12(self):
        """test integer heximal notation"""
        
        self.assertTrue(TestLexer.test("0x1234567890","0x1234567890,<EOF>",142))
        
    def test_integer13(self):
        """test integer heximal notation"""
        
        self.assertTrue(TestLexer.test("0x024EF234AAA","0x024EF234AAA,<EOF>",143))
        
    def test_integer14(self):
        """test integer heximal notation"""
        
        self.assertTrue(TestLexer.test("0x__02_4_EF_23_4AA_A","0x024EF234AAA,<EOF>",144))
        
    def test_integer15(self):
        """test integer heximal notation"""
        
        self.assertTrue(TestLexer.test("0x__02_4_EF_23_4AA_A 0x__02_4_EF_23_4AA_A 0x__02_4_EF_23_4AA_A ","0x024EF234AAA,0x024EF234AAA,0x024EF234AAA,<EOF>",145))
        
    def test_integer16(self):
        """test integer binary form"""
        
        self.assertTrue(TestLexer.test("0b11111111","0b11111111,<EOF>",146))
        
    def test_integer17(self):
        """test integer binary form"""
        
        self.assertTrue(TestLexer.test("0B0101001","0B0101001,<EOF>",147))
        
    def test_integer18(self):
        """test integer binary form"""
        
        self.assertTrue(TestLexer.test("0b0_011__10_01","0b00111001,<EOF>",148))
        
    def test_integer19(self):
        """test integer binary form"""
        
        self.assertTrue(TestLexer.test("0b0_011__10_01 0b0_011__10_01 0b0_011__10_01","0b00111001,0b00111001,0b00111001,<EOF>",149))
        
    def test_integer20(self):
        """test integer binary form"""
        
        self.assertTrue(TestLexer.test("0123 0XABEF123 0B01_01110  123_456_537","0123,0XABEF123,0B0101110,123456537,<EOF>",150))
        
    
    
    def test_float1(self):
        """test float focus integer part"""
        
        self.assertTrue(TestLexer.test("123456.2e3","123456.2e3,<EOF>",151))
        
    def test_float2(self):
        """test float focus integer part"""
        
        self.assertTrue(TestLexer.test("1___.2e3","1.2e3,<EOF>",152))
        
    def test_float3(self):
        """test float focus integer part"""
        
        self.assertTrue(TestLexer.test("1__23__45___6.2e3","123456.2e3,<EOF>",153))
        
    def test_float4(self):
        """test float focus integer part"""
        
        self.assertTrue(TestLexer.test("1___2345___6.2e3","123456.2e3,<EOF>",154))
        
    def test_float5(self):
        """test float focus integer part"""
        
        self.assertTrue(TestLexer.test("100__0000__.2e3","1000000.2e3,<EOF>",155))
        
    
    def test_float6(self):
        """test float focus decimal part"""
        
        self.assertTrue(TestLexer.test("1___.e3","1.e3,<EOF>",156))
        
    def test_float7(self):
        """test float focus decimal part"""
        
        self.assertTrue(TestLexer.test("1___.034e3","1.034e3,<EOF>",157))
        
    def test_float8(self):
        """test float focus decimal part"""
        
        self.assertTrue(TestLexer.test("1___.338719845e3","1.338719845e3,<EOF>",158))
        
    def test_float9(self):
        """test float focus decimal part"""
        
        self.assertTrue(TestLexer.test("1___.00000e3","1.00000e3,<EOF>",159))
        
    def test_float10(self):
        """test float focus decimal part"""
        
        self.assertTrue(TestLexer.test("1___.3422211e3","1.3422211e3,<EOF>",160))
        
    def test_float11(self):
        """test float focus exp part"""
        
        self.assertTrue(TestLexer.test("1___.56e123","1.56e123,<EOF>",161))
        
    def test_float12(self):
        """test float focus exp part"""
        
        self.assertTrue(TestLexer.test("1___.56e+123","1.56e+123,<EOF>",162))
        
    def test_float13(self):
        """test float focus exp part"""
        
        self.assertTrue(TestLexer.test("1___.56e-123","1.56e-123,<EOF>",163))
        
    def test_float14(self):
        """test float focus exp part"""
        
        self.assertTrue(TestLexer.test("1___.56E-00298","1.56E-00298,<EOF>",164))
        
    def test_float15(self):
        """test float focus exp part"""
        
        self.assertTrue(TestLexer.test("1___.56E-000001","1.56E-000001,<EOF>",165))
        
    def test_float16(self):
        """test float incomplete form"""
        
        self.assertTrue(TestLexer.test("7E-10","7E-10,<EOF>",166))
        
    def test_float17(self):
        """test float incomplete form"""
        
        self.assertTrue(TestLexer.test("7_08_5E-000001","7085E-000001,<EOF>",167))
        
    def test_float18(self):
        """test float incomplete form"""
        
        self.assertTrue(TestLexer.test("7440.35","7440.35,<EOF>",168))
        
    def test_float19(self):
        """test float incomplete form"""
        
        self.assertTrue(TestLexer.test(".001E-001",".001E-001,<EOF>",169))
        
    def test_float20(self):
        """test float incomplete form"""
        
        self.assertTrue(TestLexer.test(".E-001",".E-001,<EOF>",170))
    
    def test_error1(self):
        """Test unclose string"""
    
        self.assertTrue(TestLexer.test(""" "abc""","Unclosed String: abc",171))
    
    def test_error2(self):
        self.assertTrue(TestLexer.test("var x = \"abc\
var y = \"abcd\"@@@@@@@","var,x,=,abcvar y = ,abcd,Unclosed String: @@@@@@@",172))
        
    def test_error3(self):
        self.assertTrue(TestLexer.test(""" "abc\ndef" ""","Unclosed String: abc",173))
        
    def test_error4(self):
        self.assertTrue(TestLexer.test("\"abc\"\n \t \"abc\tcdf\"","abc,Unclosed String: abc",174))
     
    def test_error5(self):
        self.assertTrue(TestLexer.test("\"abcbcd\\","Unclosed String: abcbcd",175))
        
    def test_error6(self):
        self.assertTrue(TestLexer.test("\"\t@@@@@@@@@@@@@@@@@@@\"","Unclosed String: ",176))
        
    def test_error7(self):
        self.assertTrue(TestLexer.test("\"abc\"cdf\"","abc,cdf,Unclosed String: ",177))
                                                    
    def test_error8(self):
        self.assertTrue(TestLexer.test("\"@@@@@\f\"","Unclosed String: @@@@@",178))
    
    def test_error9(self):
        self.assertTrue(TestLexer.test("\"String with single quote \'this is good\'\"","Unclosed String: String with single quote \'this is good\'\"",179))
        
    def test_error10(self):
        self.assertTrue(TestLexer.test("\"@@@@@@@\r\t\f\b\"","Unclosed String: @@@@@@@",180))        
        
    
    def test_error11(self):
        """Test illegal escape"""
        
        self.assertTrue(TestLexer.test("\"@@@@@@\\\"","Illegal Escape In String: @@@@@@\\\"",181))
        
    def test_error12(self):
        """Test illegal escape"""
        
        self.assertTrue(TestLexer.test("\"abc\\h def\"","Illegal Escape In String: abc\\h",182))
        
    def test_error13(self):
        """Test illegal escape"""
        
        self.assertTrue(TestLexer.test("\"abc\\xyz\"","Illegal Escape In String: abc\\x",183))
        
    def test_error14(self):
        """Test illegal escape"""
        
        self.assertTrue(TestLexer.test("\"Tran Manh Dung\\\"","Illegal Escape In String: Tran Manh Dung\\\"",184))
        
    def test_error15(self):
        """Test illegal escape"""
        
        self.assertTrue(TestLexer.test("\"\\habc\"","Illegal Escape In String: \\h",185))
     
    def test_error16(self):
        """Test error token"""
        
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",186))
                                                
    def test_error17(self):
        """Test error token"""
        
        self.assertTrue(TestLexer.test("$ab@vn","$ab,Error Token @",187))
        
    def test_error18(self):
        """Test error token"""
        
        self.assertTrue(TestLexer.test("@@@@@@@","Error Token @",188))
        
    def test_error19(self):
        """Test error token"""
        
        self.assertTrue(TestLexer.test("&abc","Error Token &",189))
        
    def test_error20(self):
        """Test error token"""
        
        self.assertTrue(TestLexer.test("var jame~~~~","var,jame,Error Token ~",190))
        
        
    def test1(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}            
""",
            r"Class,Rectangle,:,Shape,{,getArea,(,),{,Return,Self,.,length,*,Self,.,width,;,},},<EOF>",
            191
        ))
        
    def test2(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Class main{}
"""
    ,
                r"Class,main,{,},<EOF>",
                192
            ))
        
    def test3(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Array (
Array("Volvo", "22", "18"),
Array("Saab", "5", "2"),
Array("Land Rover", "17", "15")
)
"""
    ,
                r"Array,(,Array,(,Volvo,,,22,,,18,),,,Array,(,Saab,,,5,,,2,),,,Array,(,Land Rover,,,17,,,15,),),<EOF>",
                193
            ))
        
    def test4(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Array(1, 5, 7, 12) && Array("Kangxi", "Yongzheng", "Qianlong")
"""
    ,
                r"Array,(,1,,,5,,,7,,,12,),&&,Array,(,Kangxi,,,Yongzheng,,,Qianlong,),<EOF>",
                194
            ))
        
    def test5(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
{
    var r, s: Int;
    r = 2.0;
    var a, b: Array[Int, 5];
    s = r * r * Self.myPI;
    a[0] = s;
}
"""
    ,
                r"{,var,r,,,s,:,Int,;,r,=,2.0,;,var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},<EOF>",
                195
            ))
            
    def test6(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Foreach (x In 5 .. 2) {
    Out.printInt(arr[x]);
}
"""
    ,
                r"Foreach,(,x,In,5,..,2,),{,Out,.,printInt,(,arr,[,x,],),;,},<EOF>",
                196
            ))
            
    def test7(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Class Shape:abc {
    Val $numOfShape: Int = 0;
    Val immutableAttribute: Int = 0;
    Var length, width: Int;
    $getNumOfShape() {
        Return $numOfShape;     
}

CLass Rectangle: Shape {
    getArea() {
    Return Self.length * Self.width;
    }
}

Class Program {
    main() {
        Out.printInt(Shape::$numOfShape);
    }
}
"""
    ,
                r"Class,Shape,:,abc,{,Val,$numOfShape,:,Int,=,0,;,Val,immutableAttribute,:,Int,=,0,;,Var,length,,,width,:,Int,;,$getNumOfShape,(,),{,Return,$numOfShape,;,},CLass,Rectangle,:,Shape,{,getArea,(,),{,Return,Self,.,length,*,Self,.,width,;,},},Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>",
                197
            ))
            
    def test8(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
Constructor (a,b,$ax,5){
     If(a > 5)
     {
         BET::print(a)
     }
}
"""
    ,
                r"Constructor,(,a,,,b,,,$ax,,,5,),{,If,(,a,>,5,),{,BET,::,print,(,a,),},},<EOF>",
                198
            ))
            
    def test9(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
if((3+5)>7)
{
     class::$a = class::$a + 1;
}
Elseif(3+7<3)
{    
}
Elseif()
{
}
Else{
}
"""
    ,
                r"if,(,(,3,+,5,),>,7,),{,class,::,$a,=,class,::,$a,+,1,;,},Elseif,(,3,+,7,<,3,),{,},Elseif,(,),{,},Else,{,},<EOF>",
                199
            ))
            
    def test10(self):
        """General test"""
            
        self.assertTrue(TestLexer.test(
            r"""
if((3+5)>7)
{
     class::$a = class::$a + 1;
}
Elseif(3+7<3)
{  
var r, s: Int;
r = 2.0;
var a, b: Array[Int, 5];
s = r * r * Self.myPI;
a[0] = s;  
}
Elseif()
{
var r, s: Int;
r = 2.0;
var a, b: Array[Int, 5];
s = r * r * Self.myPI;
a[0] = s;
}
Else{
} 
"""
    ,
                r"if,(,(,3,+,5,),>,7,),{,class,::,$a,=,class,::,$a,+,1,;,},Elseif,(,3,+,7,<,3,),{,var,r,,,s,:,Int,;,r,=,2.0,;,var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},Elseif,(,),{,var,r,,,s,:,Int,;,r,=,2.0,;,var,a,,,b,:,Array,[,Int,,,5,],;,s,=,r,*,r,*,Self,.,myPI,;,a,[,0,],=,s,;,},Else,{,},<EOF>",
                200
            ))                                                            
                                                       
                                                                                
        
                                                                                                                         
