from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.gunpla import Gunpla
from app.forms.gunpla import GunplaForm
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    gunplas = Gunpla.query.all()
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
    gunpla = Gunpla.query.get_or_404(gunpla_id)
    form = GunplaForm(obj=gunpla)
    if form.validate_on_submit():
        gunpla.name = form.name.data
        gunpla.series = form.series.data
        gunpla.grade = form.grade.data
        gunpla.scale = form.scale.data
        db.session.commit()
        flash('Gunpla model updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('gunpla/edit.html', form=form)

@bp.route('/delete/<int:gunpla_id>', methods=['POST'])
def delete(gunpla_id):
    gunpla = Gunpla.query.get_or_404(gunpla_id)
    db.session.delete(gunpla)
    db.session.commit()
    flash('Gunpla model deleted successfully!', 'success')
    return redirect(url_for('main.index'))