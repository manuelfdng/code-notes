# routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, abort, jsonify
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

@main.route('/gunpla/<int:gunpla_id>/edit-form', methods=['GET'])
def get_edit_form(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    form = GunplaForm(obj=gunpla)
    return render_template('edit_form.html', form=form, gunpla=gunpla)

@main.route('/gunpla/<int:gunpla_id>/row', methods=['GET'])
def get_gunpla_row(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    return render_template('gunpla_row.html', gunpla=gunpla)

@main.route('/delete/<int:gunpla_id>', methods=['POST', 'DELETE'])
def delete(gunpla_id):
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    db.session.delete(gunpla)
    db.session.commit()
    # Flash message will be cleared by the event listener
    flash('Gunpla model deleted successfully!', 'success')
    return ""

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
        # Flash message will be cleared by the event listener
        flash('Gunpla model updated successfully!', 'success')
        return render_template('gunpla_row.html', gunpla=gunpla)
    if form.errors:
        return render_template('edit_form.html', form=form, gunpla=gunpla), 422
    return render_template('edit_form.html', form=form, gunpla=gunpla)