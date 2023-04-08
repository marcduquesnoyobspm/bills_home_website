from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    DateField,
    SelectField,
    HiddenField,
)
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Regexp
from ..models.user import User
from sqlalchemy import func
from .catalogue import entreprises
from itertools import chain


class LoginForm(FlaskForm):
    identifiant = StringField("Email ou identifiant", validators=[DataRequired()])

    password = PasswordField("Password", validators=[DataRequired()])

    remember_me = BooleanField("Remember Me")

    submit = SubmitField("Sign In")


class StartRegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])

    submit = SubmitField("Commencer >")

    def validate_email(self, email):
        user = User.query.filter_by(user_email=email.data).first()

        if user is not None:
            raise ValidationError("Cette adresse email est déjà utilisée.")

        else:
            user = User.query.filter_by(user_identifiant=email.data).first()

            if user is not None:
                raise ValidationError("Cette adresse email est déjà utilisée.")


class FinalRegistrationForm(FlaskForm):
    password = PasswordField(
        "Mot de passe",
        validators=[
            DataRequired(),
            Regexp(
                regex="^(?=.*([A-Z]){1,})(?=.*[!@#$&*]{1,})(?=.*[0-9]{1,})(?=.*[a-z]{1,}).{8,}$"
            ),
        ],
        render_kw={"autocomplete": "new-password"},
    )

    remember_me = BooleanField("Se souvenir de moi")

    recaptcha = RecaptchaField()

    submit = SubmitField("S'inscrire")


class MoreInfosRegistrationForm(FlaskForm):
    identifiant = StringField("Identifiant", validators=[DataRequired()])

    first_name = StringField("Prénom")

    last_name = StringField("Nom")

    submit = SubmitField(
        "Poursuivre >", render_kw={"onclick": "submit_more_infos_form(event)"}
    )

    def validate_identifiant(self, identifiant):
        user = User.query.filter_by(
            user_identifiant=func.binary(identifiant.data)
        ).first()

        if user is not None:
            raise ValidationError("Please use a different identifiant.")

        else:
            user = User.query.filter_by(user_email=identifiant.data).first()

            if user is not None:
                raise ValidationError("Please use a different identifiant.")


class OverviewUpdateProfileForm(FlaskForm):
    first_name = StringField("Prénom")

    last_name = StringField("Nom")

    submit = SubmitField(
        "Modifier son profil",
        render_kw={"onclick": "submitOverviewUpdateProfileForm(event)"},
    )


class UpdateProfileImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired(),
            FileAllowed(
                [
                    "jpg",
                    "png",
                    "jpeg",
                ],
                "Le fichier doit être sous le format .jpeg, .jpg ou .png",
            ),
        ],
        render_kw={"onchange": "send_image_form_data(event)"},
    )


class UpdateProfileEmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField(
        "Mot de passe",
        validators=[DataRequired()],
        render_kw={"autocomplete": "new-password"},
    )

    submit = SubmitField(
        "Modifier son profil", render_kw={"onclick": "send_email_form_data(event)"}
    )

    def validate_email(self, email):
        user = User.query.filter_by(user_email=email.data).first()

        if user is not None and user.user_email != current_user.user_email:
            raise ValidationError("Please use a different email address.")

        else:
            user = User.query.filter_by(user_identifiant=email.data).first()

            if user is not None:
                raise ValidationError("Please use a different email address.")


class UpdateProfileInfosForm(FlaskForm):
    first_name = StringField("Prénom")

    last_name = StringField("Nom")

    submit = SubmitField(
        "Modifier son profil", render_kw={"onclick": "send_infos_form_data(event)"}
    )


class UpdateProfileIdentifiantForm(FlaskForm):
    identifiant = StringField("Identifiant", validators=[DataRequired()])

    password = PasswordField(
        "Mot de passe actuel",
        validators=[DataRequired()],
        render_kw={"autocomplete": "new-password"},
    )

    submit = SubmitField(
        "Modifier son profil",
        render_kw={"onclick": "send_identifiant_form_data(event)"},
    )

    def validate_identifiant(self, identifiant):
        user = User.query.filter(
            User.user_identifiant == func.binary(identifiant.data)
        ).first()

        if user is not None and user.user_identifiant != current_user.user_identifiant:
            print(user.user_identifiant, current_user.user_identifiant)

            raise ValidationError("Please use a different identifiant.")

        else:
            user = User.query.filter_by(user_email=identifiant.data).first()

            if user is not None:
                raise ValidationError("Please use a different identifiant.")


class UpdateProfilePasswordForm(FlaskForm):
    current_password = PasswordField(
        "Mot de passe actuel",
        validators=[DataRequired()],
        render_kw={"autocomplete": "new-password"},
    )

    future_password = PasswordField(
        "Futur mot de passe",
        validators=[
            DataRequired(),
            Regexp(
                regex="^(?=.*([A-Z]){1,})(?=.*[!@#$&*]{1,})(?=.*[0-9]{1,})(?=.*[a-z]{1,}).{8,}$"
            ),
        ],
        render_kw={"autocomplete": "new-password"},
    )

    confirmation_future_password = PasswordField(
        "Confirmation du futur mot de passe",
        validators=[DataRequired(), EqualTo("future_password")],
        render_kw={"autocomplete": "new-password"},
    )

    submit = SubmitField(
        "Modifier son profil", render_kw={"onclick": "send_password_form_data(event)"}
    )


class DeleteProfileForm(FlaskForm):
    identifiant = StringField(
        "Identifiant ou adresse e-mail", validators=[DataRequired()]
    )

    password = PasswordField(
        "Mot de passe actuel",
        validators=[DataRequired()],
        render_kw={"autocomplete": "new-password"},
    )

    submit = SubmitField("Modifier son profil")

    def validate_identifiant(self, identifiant):
        if identifiant.data not in [
            current_user.user_identifiant,
            current_user.user_email,
        ]:
            raise ValidationError("Identifiant ou adresse e-mail incorrect.")


class AddContractForm(FlaskForm):
    category_choices = list(entreprises.keys())

    category = SelectField(
        "Catégorie du contrat",
        choices=[""] + category_choices,
        validators=[DataRequired()],
        render_kw={"onchange": "categorySelected()"},
    )

    name = StringField("Nom du contrat")

    entreprise = SelectField(
        "Entreprise",
        choices=list(
            chain.from_iterable(
                [""]
                + [
                    list(entreprises[category].keys())
                    for category in list(entreprises.keys())
                ]
            )
        ),
        validators=[DataRequired()],
        render_kw={"onchange": "entrepriseSelected()"},
    )

    identifiant = StringField("Identifiant de votre compte sur le site de l'entreprise")

    password = PasswordField(
        "Mot de passe de votre compte sur le site de l'entreprise",
        render_kw={"autocomplete": "new-password"},
    )

    num_contract = StringField("Numéro du contrat")

    mens = StringField(
        "Montant de la mensualité",
        render_kw={"oninput": "testDecimalNumber()"},
    )

    date = DateField("Date de renouvellement du contrat")

    more_infos = StringField("Plus d'informations sur le contrat")

    submit = SubmitField("Ajouter le contrat")


class ShowContractForm(FlaskForm):
    name = StringField("Nom du contrat", render_kw={"readonly": True})

    entreprise = StringField("Entreprise", render_kw={"readonly": True})

    identifiant = StringField(
        "Identifiant de votre compte sur le site de l'entreprise",
        render_kw={"readonly": True},
    )

    password = PasswordField(
        "Mot de passe de votre compte sur le site de l'entreprise",
        render_kw={"readonly": True},
    )

    num_contract = StringField("Numéro du contrat", render_kw={"readonly": True})

    mens = StringField("Montant de la mensualité", render_kw={"readonly": True})

    date = DateField("Date de renouvellement du contrat", render_kw={"readonly": True})

    more_infos = StringField(
        "Plus d'informations sur le contrat", render_kw={"readonly": True}
    )


class UpdateContractForm(FlaskForm):
    name = StringField("Nom du contrat")

    entreprise = StringField("Entreprise")

    identifiant = StringField("Identifiant de votre compte sur le site de l'entreprise")

    password = PasswordField("Mot de passe de votre compte sur le site de l'entreprise")

    num_contract = StringField("Numéro du contrat")

    mens = StringField(
        "Montant de la mensualité",
        render_kw={"oninput": "testDecimalNumber()"},
    )

    date = DateField("Date de renouvellement du contrat")

    more_infos = StringField("Informations complémentaires")

    update_submit = SubmitField("Modifier le contrat")
