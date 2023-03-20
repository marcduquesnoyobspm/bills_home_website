from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from ..models.user import User


class LoginForm(FlaskForm):

    email = StringField('Email ou identifiant', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):

    identifiant = StringField('Identifiant', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    password2 = PasswordField('Repeat Password', validators=[
                              DataRequired(), EqualTo('password')])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Register')

    def validate_identifiant(self, identifiant):

        user = User.query.filter_by(user_identifiant=identifiant.data).first()

        if user is not None:

            raise ValidationError('Please use a different identifiant.')

        else:

            user = User.query.filter_by(user_email=identifiant.data).first()

            if user is not None:

                raise ValidationError('Please use a different identifiant.')

    def validate_email(self, email):

        user = User.query.filter_by(user_email=email.data).first()

        if user is not None:

            raise ValidationError('Please use a different email address.')

        else:

            user = User.query.filter_by(user_identifiant=email.data).first()

            if user is not None:

                raise ValidationError('Please use a different email address.')


class AddContractForm(FlaskForm):

    category_choices = ["Electricité", "Gaz", "Téléphone", "Internet",
                        "Assurance animal", "Assurance Auto", "Assurance Maison"]

    category = SelectField(
        'Field name', choices=category_choices, validators=[DataRequired()])

    entreprise = StringField('Entreprise')

    url = StringField('URL')

    identifiant = StringField('Identifiant')

    password = PasswordField('Password')

    num_contract = StringField('Numéro de contrat')

    mens = DecimalField('Montant de la mensualité')

    date = DateField('Date')

    more_infos = StringField("Plus d'informations")

    submit = SubmitField('Add')
