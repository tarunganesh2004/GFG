# Expression Add Operators 

s="124"
target=9

def findExpr(s,target):
    res=[]

    def backtrack(index,cur_expr,cur_val,last_operand):
        if index==len(s):
            if cur_val==target:
                res.append(cur_expr)
            return
        
        for j in range(index,len(s)):
            operand_str=s[index:j+1]
            if len(operand_str)>1 and operand_str[0]=='0':
                break

            operand_val=int(operand_str)
            if index==0:
                backtrack(j+1,operand_str,operand_val,operand_val)
            else:
                backtrack(j+1,cur_expr+'+'+operand_str,cur_val+operand_val,operand_val)
                backtrack(j+1,cur_expr+'-'+operand_str,cur_val-operand_val,-operand_val)
                backtrack(j+1,cur_expr+'*'+operand_str,cur_val-last_operand+last_operand*operand_val,last_operand*operand_val)
    backtrack(0,"",0,0)
    return res

print(findExpr(s,target))