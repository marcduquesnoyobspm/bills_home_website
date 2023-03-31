from flask_wtf import FlaskForm, RecaptchaField
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Regexp
from ..models.user import User
from sqlalchemy import func


class LoginForm(FlaskForm):

    email = StringField('Email ou identifiant', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')
    

class StartRegistrationForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    submit = SubmitField('Commencer >')
    
    def validate_email(self, email):
        
        user = User.query.filter_by(user_email=email.data).first()

        if user is not None:

            raise ValidationError('Cette adresse email est déjà utilisée.')

        else:

            user = User.query.filter_by(user_identifiant=email.data).first()

            if user is not None:

                raise ValidationError('Cette adresse email est déjà utilisée.')


class FinalRegistrationForm(FlaskForm):
    
    password = PasswordField('Mot de passe', validators=[
        DataRequired(),
        Regexp(regex="^(?=.*([A-Z]){1,})(?=.*[!@#$&*]{1,})(?=.*[0-9]{1,})(?=.*[a-z]{1,}).{8,}$")
        ], render_kw={"autocomplete":"new-password"})
       
    remember_me = BooleanField('Se souvenir de moi')
    
    recaptcha = RecaptchaField()
    
    submit = SubmitField("S'inscrire")
            
            
class MoreInfosRegistrationForm(FlaskForm):

    identifiant = StringField('Identifiant', validators=[DataRequired()])
    
    first_name = StringField("Prénom")
    
    last_name = StringField("Nom")

    submit = SubmitField('Poursuivre >', render_kw={"onclick":"submit_more_infos_form(event)"})

    def validate_identifiant(self, identifiant):

        user = User.query.filter_by(user_identifiant=func.binary(identifiant.data)).first()

        if user is not None:

            raise ValidationError('Please use a different identifiant.')

        else:

            user = User.query.filter_by(user_email=identifiant.data).first()

            if user is not None:

                raise ValidationError('Please use a different identifiant.')


class UpdateProfileForm(FlaskForm):

    identifiant = StringField('Identifiant', validators=[DataRequired()])
    
    first_name = StringField("Prénom")
    
    last_name = StringField("Nom")

    email = StringField('Email', validators=[DataRequired(), Email()])

    current_password = PasswordField('Mot de passe actuel', validators=[DataRequired()], render_kw={"autocomplete":"new-password"})
    
    future_password = PasswordField('Futur mot de passe', validators=[
                              DataRequired()], render_kw={"autocomplete":"new-password"})

    confirmation_future_password = PasswordField('Confirmation du futur mot de passe', validators=[
                              DataRequired(), EqualTo('future_password')], render_kw={"autocomplete":"new-password"})

    submit = SubmitField('Modifier son profil')

    def validate_identifiant(self, identifiant):

        user = User.query.filter(User.user_identifiant == func.binary(identifiant.data)).first()

        if user is not None and user.user_identifiant != current_user.user_identifiant:
            
            print(user.user_identifiant, current_user.user_identifiant)

            raise ValidationError('Please use a different identifiant.')

        else:

            user = User.query.filter_by(user_email=identifiant.data).first()

            if user is not None:

                raise ValidationError('Please use a different identifiant.')

    def validate_email(self, email):

        user = User.query.filter_by(user_email=email.data).first()

        if user is not None and user.user_email != current_user.user_email:

            raise ValidationError('Please use a different email address.')

        else:

            user = User.query.filter_by(user_identifiant=email.data).first()

            if user is not None:

                raise ValidationError('Please use a different email address.')


class AddContractForm(FlaskForm):

    category_choices = ["Electricité", "Gaz", "Téléphone", "Internet",
                        "Assurance animal", "Assurance Auto", "Assurance Maison"]

    category = SelectField(
        'Catégorie du contrat', choices=category_choices, validators=[DataRequired()], render_kw = {"onchange":"gazSelected()"})

    name = StringField('Nom du contrat')
    
    entreprise = StringField('Entreprise')

    url = StringField('URL')

    identifiant = StringField("Identifiant de votre compte sur le site de l'entreprise")

    password = PasswordField("Mot de passe de votre compte sur le site de l'entreprise", render_kw={"autocomplete":"new-password"})

    num_contract = StringField('Numéro du contrat')

    mens = DecimalField('Montant de la mensualité')

    date = DateField('Date de renouvellement du contrat')

    more_infos = StringField("Plus d'informations sur le contrat")

    submit = SubmitField('Ajouter le contrat')


class UpdateContractForm(FlaskForm):

    name = StringField('Nom du contrat')
    
    entreprise = StringField('Entreprise')

    url = StringField('URL')

    identifiant = StringField("Identifiant de votre compte sur le site de l'entreprise")

    password = StringField("Mot de passe de votre compte sur le site de l'entreprise")

    num_contract = StringField('Numéro du contrat')

    mens = DecimalField('Montant de la mensualité', places = 2, rounding = 2, render_kw={"oninput":"testDecimalNumber()"})

    date = DateField('Date de renouvellement du contrat')

    more_infos = StringField("Plus d'informations sur le contrat")

    update_submit = SubmitField('Modifier le contrat')
    

class ShowContractForm(FlaskForm):
    
    name = StringField('Nom du contrat', render_kw={'readonly': True})
    
    entreprise = StringField('Entreprise', render_kw={'readonly': True})

    url = StringField('URL', render_kw={'readonly': True})

    identifiant = StringField("Identifiant de votre compte sur le site de l'entreprise", render_kw={'readonly': True})

    password = StringField("Mot de passe de votre compte sur le site de l'entreprise", render_kw={'readonly': True})

    num_contract = StringField('Numéro du contrat', render_kw={'readonly': True})

    mens = DecimalField('Montant de la mensualité', render_kw={'readonly': True})

    date = DateField('Date de renouvellement du contrat', render_kw={'readonly': True})

    more_infos = StringField("Plus d'informations sur le contrat", render_kw={'readonly': True})