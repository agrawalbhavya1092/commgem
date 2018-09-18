# Generated by Django 2.1.1 on 2018-09-11 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_column='CG_UM_EMAIL', max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, db_column='CG_UM_FIRST_NAME', max_length=255, verbose_name='first name')),
                ('pref_first_name', models.CharField(blank=True, db_column='CG_UM_PREF_FIRST_NAME', max_length=255, verbose_name='preferred first name')),
                ('emp_id', models.CharField(blank=True, db_column='CG_UM_ALTER_EMPLID', max_length=10)),
                ('last_name', models.CharField(blank=True, db_column='CG_UM_LAST_NAME', max_length=255, verbose_name='last name')),
                ('pref_last_name', models.CharField(blank=True, db_column='CG_UM_PREF_LAST_NAME', max_length=255, verbose_name='preferred last name')),
                ('middle_name', models.CharField(blank=True, db_column='CG_UM_MIDDLE_NAME', max_length=255, verbose_name='middle name')),
                ('title', models.CharField(blank=True, choices=[('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms')], db_column='CG_UM_TITLE', max_length=5, verbose_name='title')),
                ('pref_language', models.CharField(blank=True, db_column='CG_UM_PREF_LANG', max_length=3, verbose_name='preferred language')),
                ('active', models.BooleanField(db_column='CG_UM_STATUS', default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'CM_User_Prfl_tbl',
                'permissions': (('test_permission', 'To provide view facility'), ('test_permission_3', 'Cannot view')),
            },
        ),
        migrations.CreateModel(
            name='DepartmentSetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, db_column='CM_STP_SOURCE', max_length=10, null=True)),
                ('status', models.CharField(blank=True, db_column='CM_STP_STATUS', max_length=50, null=True)),
                ('department_id', models.CharField(blank=True, db_column='CM_STP_DEPTID', max_length=10, null=True)),
                ('department_name', models.CharField(blank=True, db_column='CM_STP_DEPTNAME', max_length=255, null=True)),
                ('level', models.CharField(blank=True, db_column='CM_STP_LEVEL', max_length=4, null=True)),
                ('m1_department_id', models.CharField(blank=True, db_column='CM_STP_M1_DEPT_ID', max_length=10, null=True)),
                ('m1_department_name', models.CharField(blank=True, db_column='CM_STP_M1_DEPT_NAME', max_length=255, null=True)),
                ('m2_department_id', models.CharField(blank=True, db_column='CM_STP_M2_DEPT_ID', max_length=10, null=True)),
                ('m2_department_name', models.CharField(blank=True, db_column='CM_STP_M2_DEPT_NAME', max_length=255, null=True)),
                ('m3_department_id', models.CharField(blank=True, db_column='CM_STP_M3_DEPT_ID', max_length=10, null=True)),
                ('m3_department_name', models.CharField(blank=True, db_column='CM_STP_M3_DEPT_NAME', max_length=255, null=True)),
                ('m4_department_id', models.CharField(blank=True, db_column='CM_STP_M4_DEPT_ID', max_length=10, null=True)),
                ('m4_department_name', models.CharField(blank=True, db_column='CM_STP_M4_DEPT_NAME', max_length=255, null=True)),
                ('m5_department_id', models.CharField(blank=True, db_column='CM_STP_M5_DEPT_ID', max_length=10, null=True)),
                ('m5_department_name', models.CharField(blank=True, db_column='CM_STP_M5_DEPT_NAME', max_length=255, null=True)),
                ('m6_department_id', models.CharField(blank=True, db_column='CM_STP_M6_DEPT_ID', max_length=10, null=True)),
                ('m6_department_name', models.CharField(blank=True, db_column='CM_STP_M6_DEPT_NAME', max_length=255, null=True)),
                ('m7_department_id', models.CharField(blank=True, db_column='CM_STP_M7_DEPT_ID', max_length=10, null=True)),
                ('m7_department_name', models.CharField(blank=True, db_column='CM_STP_M7_DEPT_NAME', max_length=255, null=True)),
                ('m8_department_id', models.CharField(blank=True, db_column='CM_STP_M8_DEPT_ID', max_length=10, null=True)),
                ('m8_department_name', models.CharField(blank=True, db_column='CM_STP_M8_DEPT_NAME', max_length=255, null=True)),
                ('m9_department_id', models.CharField(blank=True, db_column='CM_STP_M9_DEPT_ID', max_length=10, null=True)),
                ('m9_department_name', models.CharField(blank=True, db_column='CM_STP_M9_DEPT_NAME', max_length=255, null=True)),
                ('m10_department_id', models.CharField(blank=True, db_column='CM_STP_M10_DEPT_ID', max_length=10, null=True)),
                ('m10_department_name', models.CharField(blank=True, db_column='CM_STP_M10_DEPT_NAME', max_length=255, null=True)),
            ],
            options={
                'db_table': 'CM_Department_Setup_tbl',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(db_column='CG_ROLE_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='CG_ROLE_NAME', max_length=255, unique=True, verbose_name='name')),
                ('status', models.CharField(blank=True, db_column='CG_ROLE_STATUS', max_length=20, verbose_name='status')),
                ('description', models.TextField(blank=True, db_column='CG_ROLE_DESCRIPTION', verbose_name='description')),
            ],
            options={
                'db_table': 'Role',
            },
            managers=[
                ('objects', users.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.IntegerField(db_column='CG_PERMISSION_ID', primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(db_column='CG_PERMISSION_NAME', max_length=255, verbose_name='name')),
                ('status', models.CharField(blank=True, db_column='CG_PERMISSION_STATUS', max_length=20, verbose_name='status')),
                ('description', models.TextField(blank=True, db_column='CG_PERMISSION_DESCRIPTION', verbose_name='description')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type')),
            ],
            options={
                'db_table': 'CM_permission_tbl',
                'ordering': ('content_type__app_label', 'content_type__model', 'codename'),
            },
            managers=[
                ('objects', users.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='RolesPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(db_column='CG_ROLE_ID', on_delete=django.db.models.deletion.CASCADE, to='users.Group')),
                ('permissions', models.ForeignKey(db_column='CG_PERMISSION_ID', on_delete=django.db.models.deletion.CASCADE, to='users.Permissions')),
            ],
            options={
                'db_table': 'CM_role_perm_mapping_tbl',
            },
        ),
        migrations.CreateModel(
            name='UsersRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(db_column='CG_UM_ROLE_ID', on_delete=django.db.models.deletion.CASCADE, to='users.Group')),
                ('user', models.ForeignKey(db_column='CG_UM_ALTER_EMPLID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CM_User_roles_mapping_tbl',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(blank=True, through='users.RolesPermissions', to='users.Permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', through='users.UsersRoles', to='users.Group', verbose_name='groups'),
        ),
        migrations.AlterUniqueTogether(
            name='permissions',
            unique_together={('content_type', 'codename')},
        ),
    ]
