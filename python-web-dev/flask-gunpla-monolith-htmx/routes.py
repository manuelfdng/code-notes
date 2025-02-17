from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from models import Gunpla, db
from forms import GunplaForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    gunplas = Gunpla.query.all()
    return render_template('index.html', gunplas=gunplas)

@main.route('/create', methods=['GET', 'POST'])
def create():
    form = GunplaForm()
    if form.validate_on_submit():
        new_gunpla = Gunpla(
            name=form.name.data,
            series=form.series.data,
            grade=form.grade.data,
            scale=form.scale.data
        )
        db.session.add(new_gunpla)
        db.session.commit()
        flash('Gunpla model created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create.html', form=form)

from flask import request

from flask import request

@main.route('/edit/<int:gunpla_id>', methods=['GET', 'POST'])
def edit(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    form = GunplaForm(obj=gunpla)
    if form.validate_on_submit():
        gunpla.name = form.name.data
        gunpla.series = form.series.data
        gunpla.grade = form.grade.data
        gunpla.scale = form.scale.data
        db.session.commit()
        flash('Gunpla model updated successfully!', 'success')
        # If the request came via HTMX, return just the updated list item HTML fragment.
        if request.headers.get("HX-Request"):
            return render_template('gunpla_item.html', gunpla=gunpla)
        return redirect(url_for('main.index'))
    # If HTMX, return a partial template (without the full layout)
    if request.headers.get("HX-Request"):
         return render_template('edit_form.html', form=form, gunpla=gunpla)
    return render_template('edit.html', form=form, gunpla=gunpla)

@main.route('/delete/<int:gunpla_id>', methods=['POST', 'DELETE'])
def delete(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    db.session.delete(gunpla)
    db.session.commit()
    flash('Gunpla model deleted successfully!', 'success')
    if request.headers.get("HX-Request"):
         # Return an empty response with HTTP status 204 (No Content) so HTMX can remove the element.
         return ('', 204)
    return redirect(url_for('main.index'))