from gen.TypeCheckerListener import TypeCheckerListener
from gen.TypeCheckerParser import TypeCheckerParser


class CalculatorListener(TypeCheckerListener):
    def exitStart(self, ctx: TypeCheckerParser.StartContext):
        if ctx.getChild(0).rule_type in ["Integer", "Float", "String"]:
            print("Output is {}. Output type is {}.".format(ctx.getChild(0).value, str(ctx.getChild(0).rule_type)))
        else:
            print(ctx.getChild(0).rule_type,ctx.getChild(0).value)

    def exitFactFloat(self, ctx: TypeCheckerParser.FactFloatContext):
        ctx.rule_type = "Float"
        ctx.value = float(ctx.getText())

    def exitFactInteger(self, ctx: TypeCheckerParser.FactIntegerContext):
        ctx.rule_type = "Integer"
        ctx.value = int(ctx.getText())

    def exitFactString(self, ctx: TypeCheckerParser.FactStringContext):
        ctx.rule_type = "String"
        ctx.value = ctx.getText()[1:-1]

    def exitFactExpr(self, ctx: TypeCheckerParser.FactExprContext):
        ctx.rule_type = ctx.getChild(1).rule_type
        ctx.value = ctx.getChild(1).value

    def exitTerm3(self, ctx: TypeCheckerParser.Term3Context):
        ctx.rule_type = ctx.getChild(0).rule_type
        ctx.value = ctx.getChild(0).value

    def exitTerm2(self, ctx: TypeCheckerParser.Term2Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type

        if ctx.rule_type not in ["Integer" , "Float"]:
            ctx.value = ""
            if ctx.rule_type == "String":
                ctx.rule_type = "Type error: String cannot be divided"
        else:
            for i in range(2, ctx.getChildCount() , 2):
                rightChildType = ctx.getChild(i).rule_type
                rightChildValue = ctx.getChild(i).value
                if ctx.rule_type == "Integer":
                    if rightChildType == "Integer":
                        ctx.value = float(ctx.value) / float(rightChildValue)
                        ctx.rule_type = "Float"
                    elif rightChildType == "Float":
                        ctx.value = float(ctx.value) / rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: Integer cannot be\
                                  divided by string."
                        break
                elif ctx.rule_type == "Float":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value / float(rightChildValue)
                        ctx.rule_type = "Float"
                    elif rightChildType == "Float":
                        ctx.value = ctx.value / rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: Float cannot be divided by string."
                        break

    def exitTerm1(self, ctx: TypeCheckerParser.Term1Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type

        if ctx.rule_type not in ["Integer", "Float"]:
            ctx.value = ""
            if ctx.rule_type == "String":
                ctx.rule_type = "Type error: String cannot be multiplied."
        else:
            for i in range(2, ctx.getChildCount(), 2):
                rightChildType = ctx.getChild(i).rule_type
                rightChildValue = ctx.getChild(i).value
                if ctx.rule_type == "Integer":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value * rightChildValue
                        ctx.rule_type = "Integer"
                    elif rightChildType == "Float":
                        ctx.value = float(ctx.value) * rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: Integer cannot be multiplied in string."
                        break
                elif ctx.rule_type == "Float":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value * float(rightChildValue)
                        ctx.rule_type = "Float"
                    elif rightChildType == "Float":
                        ctx.value = ctx.value * rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: Float cannot be multiplied in string."
                        break

    def exitExpr3(self, ctx: TypeCheckerParser.Expr3Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type

    def exitExpr2(self, ctx: TypeCheckerParser.Expr2Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type

        if ctx.rule_type not in ["Integer", "Float"]:
            ctx.value = ""
            if ctx.rule_type == "String":
                ctx.rule_type = "Type error: String cannot be subtracted"
        else:
            for i in range(2, ctx.getChildCount(), 2):
                rightChildType = ctx.getChild(i).rule_type
                rightChildValue = ctx.getChild(i).value
                if ctx.rule_type == "Integer":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value - rightChildValue
                        ctx.rule_type = "Integer"
                    elif rightChildType == "Float":
                        ctx.value = float(ctx.value) - rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: Integer cannot be subtracted by string."
                        break
                elif ctx.rule_type == "Float":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value - float(rightChildValue)
                        ctx.rule_type = "Float"
                    elif rightChildType == "Float":
                        ctx.value = ctx.value - rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: Float cannot be subtracted by string."
                        break

    def exitExpr1(self, ctx: TypeCheckerParser.Expr1Context):
        ctx.value = ctx.getChild(0).value
        ctx.rule_type = ctx.getChild(0).rule_type
        if ctx.rule_type in ["Integer", "Float", "String"]:
            for i in range(2, ctx.getChildCount(), 2):
                rightChildType = ctx.getChild(i).rule_type
                rightChildValue = ctx.getChild(i).value
                if ctx.rule_type == "Integer":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value + rightChildValue
                        ctx.rule_type = "Integer"
                    elif rightChildType == "Float":
                        ctx.value = float(ctx.value) + rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: String cannot be concatenated to an Integer"
                        break
                elif ctx.rule_type == "Float":
                    if rightChildType == "Integer":
                        ctx.value = ctx.value + float(rightChildValue)
                        ctx.rule_type = "Float"
                    elif rightChildType == "Float":
                        ctx.value = ctx.value + rightChildValue
                        ctx.rule_type = "Float"
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        if rightChildType == "String":
                            ctx.rule_type = "Type error: String cannot be concatenated to a Float"
                        break
                elif ctx.rule_type == "String":
                    if rightChildType in ["String", "Integer", "Float"]:
                        ctx.value = ctx.value + str(rightChildValue)
                    else:
                        ctx.value = ""
                        ctx.rule_type = rightChildType
                        break
