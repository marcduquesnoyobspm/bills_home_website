from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from datetime import date
from ..models import db
from ..models.contract import Contract
from ..models.user import User
from ..utils.forms import AddContractForm, UpdateContractForm, ShowContractForm


contract = Blueprint('contract', __name__)


@contract.route('/contract/add', methods=['GET', 'POST'])
@login_required
def add_contract():
    form = AddContractForm()
    if form.validate_on_submit():
        contract = Contract(contract_category=form.category.data,
                            contract_name=form.name.data, 
                            contract_entreprise=form.entreprise.data, 
                            contract_url=form.url.data,
                            contract_mens=form.mens.data, 
                            contract_date=form.date.data, 
                            contract_more_infos=form.more_infos.data, 
                            user=current_user,
                            contract_popularity = 0,
                            contract_date_creation = date.today()
                            )
        contract.set_identifiant(form.identifiant.data)
        contract.set_password(form.password.data)
        contract.set_num(form.num_contract.data)
        db.session.add(contract)
        db.session.commit()
        return redirect(url_for('controllers.overview.overview_page'))
    return render_template('add_contract.html', form=form)


@contract.route('/contract/<id>', methods=['GET'])
@login_required
def show_contract(id):
    form = ShowContractForm()
    contract_to_show = db.session.query(Contract).filter(Contract.id == id, Contract.user_id == current_user.id).first()
    identifiant = contract_to_show.get_identifiant()
    password = contract_to_show.get_password()
    num = contract_to_show.get_num()
    return render_template("show_contract.html", form=form, contract_to_show=contract_to_show, identifiant=identifiant, password=password, num=num)


@contract.route('/contract/update/<id>', methods=['GET','POST'])
@login_required
def update_contract(id):
    form = UpdateContractForm()
    contract_to_show = db.session.query(Contract).filter(Contract.id == id, Contract.user_id == current_user.id).first()
    identifiant = contract_to_show.get_identifiant()
    password = contract_to_show.get_password()
    num = contract_to_show.get_num()
    if form.validate_on_submit():
        contract_to_show.contract_entreprise = form.entreprise.data
        contract_to_show.contract_url = form.url.data
        contract_to_show.contract_mens = form.mens.data
        contract_to_show.contract_date = form.date.data
        contract_to_show.contract_more_infos = form.more_infos.data
        contract_to_show.set_identifiant(form.identifiant.data)
        contract_to_show.set_password(form.password.data)
        contract_to_show.set_num(form.num_contract.data)
        db.session.add(contract_to_show)
        db.session.commit()
        return redirect(url_for('controllers.overview.overview_page'))
    return render_template('update_contract.html', form=form, contract_to_show=contract_to_show, identifiant=identifiant, password=password, num=num)


@contract.route('/contract/delete/<id>', methods=['GET'])
@login_required
def delete_contract(id):
    contract_to_delete = db.session.query(Contract).filter(Contract.id == id, Contract.user_id == current_user.id).first()
    if contract_to_delete is None:
        flash("Erreur")
        return redirect(url_for('controllers.overview.overview_page'))
    else:
        db.session.delete(contract_to_delete)
        db.session.commit()
    return redirect(url_for('controllers.overview.overview_page'))
