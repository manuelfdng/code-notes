# app/routes/main.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from app.models.gunpla import Gunpla
from app.forms.gunpla import GunplaForm
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    gunplas = db.session.execute(db.select(Gunpla)).scalars().all()
    return render_template('gunpla/index.html', gunplas=gunplas)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = GunplaForm()
    if form.validate_on_submit():
        gunpla = Gunpla(
            name=form.name.data,
            series=form.series.data,
            grade=form.grade.data,
            scale=form.scale.data
        )
        db.session.add(gunpla)
        db.session.commit()
        flash('Gunpla model added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('gunpla/create.html', form=form)

@bp.route('/edit/<int:gunpla_id>', methods=['GET', 'POST'])
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
        return render_template('gunpla/gunpla_row.html', gunpla=gunpla)
    return render_template('gunpla/edit_form.html', form=form, gunpla=gunpla)

@bp.route('/delete/<int:gunpla_id>', methods=['POST'])
def delete(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    db.session.delete(gunpla)
    db.session.commit()
    flash('Gunpla model deleted successfully!', 'success')
    return ''  # Return empty response for HTMX to remove the element

@bp.route('/gunpla/<int:gunpla_id>/edit-form')
def get_edit_form(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    form = GunplaForm(obj=gunpla)
    return render_template('gunpla/edit_form.html', form=form, gunpla=gunpla)

@bp.route('/gunpla/<int:gunpla_id>')
def get_gunpla_row(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    return render_template('gunpla/gunpla_row.html', gunpla=gunpla)