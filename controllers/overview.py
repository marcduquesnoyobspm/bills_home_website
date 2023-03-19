from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required
from ..models import db
from ..models.contract import Contract
from ..utils.forms import AddContractForm


overview = Blueprint('overview', __name__)

@overview.route('/overview')
@login_required
def overview_page():
    return render_template('overview.html')


@overview.route('/add_contract', methods=['GET', 'POST'])
@login_required
def add_contract():
    form = AddContractForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("JE SUIS LA")
        first_user = [current_user]
        print(form.date.data)
        contract = Contract(contract_category=form.category.data, contract_entreprise=form.entreprise.data, contract_url=form.url.data, contract_mens=form.mens.data, contract_date=form.date.data, contract_more_infos=form.more_infos.data, users=first_user)
        contract.set_identifiant(form.identifiant.data)
        contract.set_password(form.password.data)
        contract.set_num(form.num_contract.data)
        db.session.add(contract)
        db.session.commit()
        flash('Congratulations, you add a new contract!')
        return redirect(url_for('overview.overview_page'))
    return render_template('add_contract.html', title='Register', form=form)