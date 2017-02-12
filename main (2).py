
def index():

        head = ''' <HTML>
					<HEAD>
					<TITLE></TITLE>
					</HEAD>

					<BODY>
					<table border="1">'''

        for i in xrange(50):
                body ='''
      <tr>
        <th>%s</th>
        <th>%s</th>
        <th>%s</th>
      </tr>
                ''' %(i,i^2,i^3)




        foot = '''	</table>
					</BODY>
					</HTML>'''

        return head + body + foot





