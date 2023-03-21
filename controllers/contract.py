from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from ..models import db
from ..models.asso_user_contract import association_table
from ..models.contract import Contract
from ..models.user import User
from ..utils.forms import AddContractForm


contract = Blueprint('contract', __name__)


@contract.route('/contract/add', methods=['GET', 'POST'])
@login_required
def add_contract():
    form = AddContractForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        first_user = [current_user]
        print(form.date.data)
        contract = Contract(contract_category=form.category.data, contract_entreprise=form.entreprise.data, contract_url=form.url.data,
                            contract_mens=form.mens.data, contract_date=form.date.data, contract_more_infos=form.more_infos.data, users=first_user)
        contract.set_identifiant(form.identifiant.data)
        contract.set_password(form.password.data)
        contract.set_num(form.num_contract.data)
        db.session.add(contract)
        db.session.commit()
        flash('Congratulations, you add a new contract!')
        return redirect(url_for('overview.overview_page'))
    return render_template('add_contract.html', form=form)


@contract.route('/contract/update/<id>', methods=['GET'])
@login_required
def update_contract():
    return redirect(url_for('overview.overview_page'))


@contract.route('/contract/delete/<id>', methods=['GET'])
@login_required
def delete_contract(id):
    contract_to_delete = db.session.query(Contract).join(Contract.users).filter(Contract.id == id, User.id == current_user.id).first()
    if contract_to_delete is None:
        pass
    else:
        db.session.delete(contract_to_delete)
        db.session.commit()
    return redirect(url_for('overview.overview_page'))
