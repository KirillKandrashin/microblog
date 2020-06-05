            {% if current_user.username != post.author.username %}
            {% if not current_user.is_liking(post.id) %}
            <p>
                <form action="{{ url_for('like') }}" method="Post">
                    {{ form.hidden_tag() }}
                    {{ form.submit(value='Like', class_='btn btn-default') }}
                </form>
            </p>
            {% else %}
            <p>
                <form action="{{ url_for('unlike') }}" method="Post">
                    {{ form.hidden_tag() }}
                    {{ form.submit(value='Unlike', class_='btn btn-default') }}
                </form>
            </p>
            {% endif %}
            {% endif %}
            
            
models.py
    
class Likers(db.Model):
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('liker_id', db.Integer, db.ForeignKey('user.id'))
    
class Post
liked = db.relationship(
        'Post', secondary=likers,
        primaryjoin=(likers.c.post_id == id),
        backref=db.backref('likers', lazy='dynamic'), lazy='dynamic')



class User:
    liked = db.relationship(
            'Likers', backref='author', lazy='dynamic')
            #primaryjoin=(likers.c.liker_id == id),
            #secondaryjoin=(likers.c.post_id == id),
            #backref=db.backref('likers', lazy='dynamic'), lazy='dynamic')
    def like(self, post):
        if not self.is_liking(post):
            self.liked.append(post)

    def unlike(self, post):
        if self.is_liking(post):
            self.liked.remove(post)

    def is_liking(self, post):
        return self.liked.filter(
            likers.c.post_id == post.id).count() > 0

_post.html



<p>{{ post.likers.count() }} likes </p>
{% if not current_user.is_liking(post) %}
<p>
<form action="{{ url_for('like', post_id=post.id) }}" method="post">
{{ form.hidden_tag() }}
{{ form.submit(value='Like', class_='btn btn-default') }}
</form>
</p>
{% endif %}




routes.py



@app.route('/like/<post_id>', methods=['POST'])
@login_required
def like(post_id):
    form = EmptyForm()
    if form.validate_on_submit():
        post = Post.query.filter_by(id=post_id).first()
        if post.author.id == current_user.id:
            flash('You cannot like your messages!')
            return redirect(url_for('index'))
        post
        current_user.like(post)
        db.session.commit()
        flash('You liked that!')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    

@app.route('/unlike/<post>', methods=['POST'])
@login_required
def unlike(post):
    form = EmptyForm()
    if form.validate_on_submit():
        if post.author.id == current_user.id:
            flash('You cannot unlike your messages!')
            return redirect(url_for('index'))
        current_user.unfollow(user)
        db.session.commit()
        flash('You took your like back')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))