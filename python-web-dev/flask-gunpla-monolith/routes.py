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

@main.route('/edit/<int:gunpla_id>', methods=['GET', 'POST'])
def edit(gunpla_id):
    # Use the new API with db.session.get()
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
        return redirect(url_for('main.index'))
    return render_template('edit.html', form=form, gunpla=gunpla)

@main.route('/delete/<int:gunpla_id>', methods=['POST'])
def delete(gunpla_id):
    # Use the new API with db.session.get()
    gunpla = db.session.get(Gunpla, gunpla_id)
    if gunpla is None:
        abort(404)
    db.session.delete(gunpla)
    db.session.commit()
    flash('Gunpla model deleted successfully!', 'success')
    return redirect(url_for('main.index'))