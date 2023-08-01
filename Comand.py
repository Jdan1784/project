# from news.models import *
#
# user1 = User.objects.create_user(username = 'Анатолий')
#
# user2 = User.objects.create_user(username = 'Мурад')
#
# Author.objects.create(authorUser = user1)
#
# Author.objects.create(authorUser = user2)
#
# Category.objects.create(name = 'Политика')
#
# Category.objects.create(name = 'Спорт')
#
# Category.objects.create(name = 'Новости кино')
#
# Category.objects.create(name = 'Интересные факты')
#
# author = Author.object.get(id = 1)
#
# author2 = Author.objects.get(id = 2)
#
# Post.objects.create(author = author, categoryType = 'AR', title='Полёт на луну', text = '«Аполло́н-11»
# (англ. Apollo 11) — американский пилотируемый космический корабль серии «Аполлон», в ходе полёта которого в
#  период с 16 по 24 июля 1969 года жители Земли впервые в истории совершили посадку на поверхность другого небесного тела — Луны.')
#
# Post.objects.create(author = author2, categoryType = 'AR', title='Странные находки в Антарктиде', text = 'При раскопках в регионе Лапаил археологи обнаружили удлиненные черепа. Открытие взбудоражило весь научный мир: необычная форма останков это еще цветочки, ведь ученые считали, что человек никогда не был в Антаркт
# иде прежде.')
#
# Post.objects.create(author = author2, categoryType = 'AR', title='Странные находки в Антарктиде', text = '')
#
# Post.objects.create(author = author, categoryType = 'NW', title='УЕФА исключил Ювентус', text = 'В результате «Ювентус» не примет участие в розыгрыше Лиги конференций 2023/2024 года. Кроме того, клуб заплатит штраф в размере 20 млн евро. Это решение последовало после расследования УЕФА, начавшегося в декабре 2022 года из-за подозрений в манипулировании финансовыми отчетами клуба и нарушении принципов финансового фэйр-плей')
#
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1), Category.objects.get(id=4))
#
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3), Category.objects.get(id=4))
#
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Советую всем прочитать, очень позновательная статья')
#
# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='Мне кажется, что это все не правда.')
#
# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Интересно, кто это был ? Может иноприщиленцы ?')
#
# Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=2).authorUser, text='Это мой любимый футбольный клуб, так не честно ! Не справедливо !!!!')
#
# Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=2).authorUser, text='Да ')
#
# Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=2).authorUser, text='Да это жестко')
#
# Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=1).authorUser, text='В жизни так бывает )')
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Comment.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).like()
#
# Post.objects.get(id=1).dislike()
#
# Post.objects.get(id=1).dislike()
#
# Post.objects.get(id=1).dislike()
#
# Post.objects.get(id=1).dislike()
#
# Post.objects.get(id=2).dislike()
#
# Post.objects.get(id=2).like()
#
# Post.objects.get(id=2).like()
#
# Post.objects.get(id=2).like()
#
# Post.objects.get(id=2).like()
#
# Post.objects.get(id=2).like()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=4).dislike()
#
# Post.objects.get(id=2).like()
#
# Post.objects.get(id=4).like()
#
# Comment.objects.get(id=3).like()
#
# Comment.objects.get(id=3).like()
#
# Comment.objects.get(id=3).like()
#
# Comment.objects.get(id=3).like()
#
# Comment.objects.get(id=3).like()
#
# Comment.objects.get(id=3).like()
#
# Comment.objects.get(id=3).dislike()
#
# a = Author.objects.get(id=1)
#
# a.update_rating()
#
# a = Author.objects.get(id=1)
#
# a.update_rating()
#
# a.ratingAuthor
#
# b = Author.objects.get(id=2)
#
# b.update_rating()
#
# b.ratingAuthor
#
# a = Author.objects.order_by('-ratingAuthor')[:1]
#
# a
#
# for i in a:
#     i.ratingAuthor
# i.authorUser.username
#
# Post.objects.order_by('-rating')[0].preview()
#
# Post.objects.order_by('-rating')[0].comment_set.all()