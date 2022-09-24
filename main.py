"""

"""

import json

from githubdata import GithubData


class GDUrl :
    with open('gdu.json' , 'r') as f :
        gj = json.load(f)

    src0 = gj['src0']
    src1 = gj['src1']
    src2 = gj['src2']
    slf = gj['slf']

gu = GDUrl()

class ColName:
    srn = 'SEORegisterNo'
    type = 'Type'
    inskind = 'InstituteKind'
    jm = 'JMonth'


c = ColName()


def main() :
    pass

    ##
    gd0  = GithubData(gu.src0)
    gd0.overwriting_clone()
    ##
    df = gd0.read_data()
    ##
    gd1 = GithubData(gu.src1)
    gd1.overwriting_clone()
    ##
    df1 = gd1.read_data()
    df1[c.srn] = df1[c.srn].astype('string')
    df1 = df1.set_index(c.srn)
    ##
    df[c.type] = df[c.srn].map(df1[c.inskind])
    ##

    gd2 = GithubData(gu.src2)
    gd2.overwriting_clone()
    ##
    df2 = gd2.read_data()
    ##
    df3 = df.groupby([c.type, c.jm]).sum()


    ##

    ##






    ##

##
if __name__ == "__main__" :
    main()
    print('Done!')
