from populate import base
from article.models import Article, Comment


titles = ['�p�󹳹q����Ǯa�@�˫��', '10�������ǦnPython', '²��ǲ�Django']
comments = ['�峹�u��', '�ä��{�P�z���[�I', '�ɤ���', '�Ǧn�@�ӵ{���y���ήج[�ä��e��']


def populate():
    print('Populating Article and Comment ... ', end='')
    Article.objects.all().delete()
    Comment.objects.all().delete()
    for title in titles:
        article = Article()
        article.title = title
        for j in range(20):
            article.content += title + '\n'
        article.save()
        for comment in comments:
            Comment.objects.create(article=article, content=comment)
    print('done')

if __name__ == '__main__':
    populate()
