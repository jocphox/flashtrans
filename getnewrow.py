
def isTitle(ss):
    if ss[0].isupper() and "." not in ss:
        return True
    elif ss[0].isupper() and "." in ss and len((ss.split(".")[0]).split(" "))>2:
        return True
    else:
        return False
def newrow(lst,pos=1):
    if pos<len(lst) and isTitle(lst[pos]):
        lst[pos:pos+1]=["\n",lst[pos]]
        newrow(lst,pos+2)
    elif pos<len(lst):
        newrow(lst,pos+1)
    else:
        pass
    return lst

if __name__ == '__main__':
    lst = ['A similar change has occurred in many other domains. Our ancestors got their',
           'thrills the old-fashioned way: they took risks. Consider the human known as the',
           'Iceman. About five thousand years ago, he set out on a European adventure and',
           'ended up frozen in a glacier. Completely preserved, he can now be visited in a', 'museum',
           'For the Iceman, a career mistake had fatal consequences. If we make a risky move',
           'say, by taking a job with some poorly financed Internet company -and it fails',
           'we will not be killed. More likely than not, we will find a new job with a higher',
           'salary. If the failure is spectacular enough, we can write a series of books, like',
           'Donald Trump. If we just rely on our instincts, we are likely to be too timid in our', 'professional lives']
    newrow(lst)
    text="".join(lst)
    newlst=text.split("\n")
    newtext="\n".join(newlst)
    print(newtext)