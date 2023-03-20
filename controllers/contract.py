from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from ..models import db
from ..models.contract import Contract
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
def delete_contract():
    return url_for('overview.overview')


@contract.route('/contract/delete/<id>', methods=['GET'])
@login_required
def delete_contract():
    return url_for('overview.overview')
