from articles.models import Article
from contact.models import ContactInformation


def contact(request):
    contact_information = ContactInformation.objects.get(allowing=True, id=1)

    return {
        'contact_information': contact_information,

    }


def recent_articles(request):
    articles = Article.objects.filter(allowing=True)[:3]

    return {
        'articles': articles,

    }
