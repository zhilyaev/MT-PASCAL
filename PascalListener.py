# Generated from antlr/Pascal.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PascalParser import PascalParser
else:
    from PascalParser import PascalParser

# This class defines a complete listener for a parse tree produced by PascalParser.
class PascalListener(ParseTreeListener):

    # Enter a parse tree produced by PascalParser#r.
    def enterR(self, ctx:PascalParser.RContext):
        pass

    # Exit a parse tree produced by PascalParser#r.
    def exitR(self, ctx:PascalParser.RContext):
        pass


    # Enter a parse tree produced by PascalParser#program.
    def enterProgram(self, ctx:PascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by PascalParser#program.
    def exitProgram(self, ctx:PascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by PascalParser#decl.
    def enterDecl(self, ctx:PascalParser.DeclContext):
        pass

    # Exit a parse tree produced by PascalParser#decl.
    def exitDecl(self, ctx:PascalParser.DeclContext):
        pass


    # Enter a parse tree produced by PascalParser#vars_decl.
    def enterVars_decl(self, ctx:PascalParser.Vars_declContext):
        pass

    # Exit a parse tree produced by PascalParser#vars_decl.
    def exitVars_decl(self, ctx:PascalParser.Vars_declContext):
        pass


    # Enter a parse tree produced by PascalParser#var_decl.
    def enterVar_decl(self, ctx:PascalParser.Var_declContext):
        pass

    # Exit a parse tree produced by PascalParser#var_decl.
    def exitVar_decl(self, ctx:PascalParser.Var_declContext):
        pass


    # Enter a parse tree produced by PascalParser#NEW_PROCEDURE.
    def enterNEW_PROCEDURE(self, ctx:PascalParser.NEW_PROCEDUREContext):
        pass

    # Exit a parse tree produced by PascalParser#NEW_PROCEDURE.
    def exitNEW_PROCEDURE(self, ctx:PascalParser.NEW_PROCEDUREContext):
        pass


    # Enter a parse tree produced by PascalParser#args_decl.
    def enterArgs_decl(self, ctx:PascalParser.Args_declContext):
        pass

    # Exit a parse tree produced by PascalParser#args_decl.
    def exitArgs_decl(self, ctx:PascalParser.Args_declContext):
        pass


    # Enter a parse tree produced by PascalParser#arg_decl.
    def enterArg_decl(self, ctx:PascalParser.Arg_declContext):
        pass

    # Exit a parse tree produced by PascalParser#arg_decl.
    def exitArg_decl(self, ctx:PascalParser.Arg_declContext):
        pass


    # Enter a parse tree produced by PascalParser#body.
    def enterBody(self, ctx:PascalParser.BodyContext):
        pass

    # Exit a parse tree produced by PascalParser#body.
    def exitBody(self, ctx:PascalParser.BodyContext):
        pass


    # Enter a parse tree produced by PascalParser#simple_body.
    def enterSimple_body(self, ctx:PascalParser.Simple_bodyContext):
        pass

    # Exit a parse tree produced by PascalParser#simple_body.
    def exitSimple_body(self, ctx:PascalParser.Simple_bodyContext):
        pass


    # Enter a parse tree produced by PascalParser#b_if.
    def enterB_if(self, ctx:PascalParser.B_ifContext):
        pass

    # Exit a parse tree produced by PascalParser#b_if.
    def exitB_if(self, ctx:PascalParser.B_ifContext):
        pass


    # Enter a parse tree produced by PascalParser#b_for.
    def enterB_for(self, ctx:PascalParser.B_forContext):
        pass

    # Exit a parse tree produced by PascalParser#b_for.
    def exitB_for(self, ctx:PascalParser.B_forContext):
        pass


    # Enter a parse tree produced by PascalParser#b_while.
    def enterB_while(self, ctx:PascalParser.B_whileContext):
        pass

    # Exit a parse tree produced by PascalParser#b_while.
    def exitB_while(self, ctx:PascalParser.B_whileContext):
        pass


    # Enter a parse tree produced by PascalParser#assign.
    def enterAssign(self, ctx:PascalParser.AssignContext):
        pass

    # Exit a parse tree produced by PascalParser#assign.
    def exitAssign(self, ctx:PascalParser.AssignContext):
        pass


    # Enter a parse tree produced by PascalParser#call.
    def enterCall(self, ctx:PascalParser.CallContext):
        pass

    # Exit a parse tree produced by PascalParser#call.
    def exitCall(self, ctx:PascalParser.CallContext):
        pass


    # Enter a parse tree produced by PascalParser#args_list.
    def enterArgs_list(self, ctx:PascalParser.Args_listContext):
        pass

    # Exit a parse tree produced by PascalParser#args_list.
    def exitArgs_list(self, ctx:PascalParser.Args_listContext):
        pass


    # Enter a parse tree produced by PascalParser#args.
    def enterArgs(self, ctx:PascalParser.ArgsContext):
        pass

    # Exit a parse tree produced by PascalParser#args.
    def exitArgs(self, ctx:PascalParser.ArgsContext):
        pass


    # Enter a parse tree produced by PascalParser#arg.
    def enterArg(self, ctx:PascalParser.ArgContext):
        pass

    # Exit a parse tree produced by PascalParser#arg.
    def exitArg(self, ctx:PascalParser.ArgContext):
        pass


    # Enter a parse tree produced by PascalParser#expression.
    def enterExpression(self, ctx:PascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PascalParser#expression.
    def exitExpression(self, ctx:PascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PascalParser#simple_expression.
    def enterSimple_expression(self, ctx:PascalParser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by PascalParser#simple_expression.
    def exitSimple_expression(self, ctx:PascalParser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by PascalParser#term.
    def enterTerm(self, ctx:PascalParser.TermContext):
        pass

    # Exit a parse tree produced by PascalParser#term.
    def exitTerm(self, ctx:PascalParser.TermContext):
        pass


    # Enter a parse tree produced by PascalParser#not_el.
    def enterNot_el(self, ctx:PascalParser.Not_elContext):
        pass

    # Exit a parse tree produced by PascalParser#not_el.
    def exitNot_el(self, ctx:PascalParser.Not_elContext):
        pass


    # Enter a parse tree produced by PascalParser#el.
    def enterEl(self, ctx:PascalParser.ElContext):
        pass

    # Exit a parse tree produced by PascalParser#el.
    def exitEl(self, ctx:PascalParser.ElContext):
        pass


    # Enter a parse tree produced by PascalParser#mb.
    def enterMb(self, ctx:PascalParser.MbContext):
        pass

    # Exit a parse tree produced by PascalParser#mb.
    def exitMb(self, ctx:PascalParser.MbContext):
        pass


