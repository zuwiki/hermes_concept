An illustrative Python prototype showing the basic architecture of the
Hermes web browser.

Doesn't do much yet. Next major item on the agenda: XMPP, the single most
important part of the whole thing. 

In [1]: from components import Script, Page

In [2]: page = Page("This content is somewhat meaningless.", Script(
...:     'print(page.content)\n' \
...:     'page.content = page.content.replace("somewhat", "entirely")'))

In [3]: page.content
Out[3]: 'This content is somewhat meaningless.'

In [4]: page.run()
This content is somewhat meaningless.
Out[4]: True

In [5]: page.content
Out[5]: 'This content is entirely meaningless.'

