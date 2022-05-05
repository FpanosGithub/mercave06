# Generated by Django 4.0.4 on 2022-05-05 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprovador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cambiador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('nombre', models.CharField(default='Experimental-01', max_length=100)),
                ('fecha_fab', models.DateField(auto_now_add=True)),
                ('num_cambios', models.IntegerField(default=0)),
                ('mantenimiento', models.CharField(max_length=16)),
                ('lng', models.FloatField(default=-4.692)),
                ('lat', models.FloatField(default=37.9246)),
            ],
        ),
        migrations.CreateModel(
            name='Certificador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Composicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('descripcion', models.CharField(default=' ', max_length=100)),
                ('lng', models.FloatField(default=-3.982)),
                ('lat', models.FloatField(default=40.2951)),
            ],
        ),
        migrations.CreateModel(
            name='Diseñador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de_ejes', models.BooleanField(default=False)),
                ('de_cambiadores', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de_ejes', models.BooleanField(default=False)),
                ('de_cambiadores', models.BooleanField(default=False)),
                ('de_bogies', models.BooleanField(default=False)),
                ('de_vagones', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Keeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de_ejes', models.BooleanField(default=False)),
                ('de_cambiadores', models.BooleanField(default=False)),
                ('de_bogies', models.BooleanField(default=False)),
                ('de_vagones', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('cif', models.CharField(max_length=16)),
                ('logo', models.CharField(max_length=150)),
                ('color_corporativo', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='VersionEje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('anchos', models.CharField(choices=[('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'), ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'), ('UIC-RUS-IB', 'UIC <> RUSO <> IBÉRICO'), ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)')], default='UIC-IB', max_length=12)),
                ('rueda', models.CharField(max_length=16)),
                ('cuerpo_eje', models.CharField(max_length=16)),
                ('fecha_aprovacion', models.DateField()),
                ('fecha_certificacion', models.DateField()),
                ('aprovador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.aprovador')),
                ('certificador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.certificador')),
                ('diseñador', models.ForeignKey(limit_choices_to={'de_ejes': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.diseñador')),
            ],
        ),
        migrations.CreateModel(
            name='VersionCambiador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('anchos', models.CharField(choices=[('UIC-IB', 'UIC(1435) <> IBÉRICO (1668)'), ('UIC-RUS', 'UIC(1435) <> RUSO (1520)'), ('METR-UIC', 'MÉTRICO(1000) <> UIC(1435)')], default='UIC-IB', max_length=12)),
                ('longitud_desencerrojado', models.FloatField(default=6000)),
                ('longitud_cambio_rueda', models.FloatField(default=6000)),
                ('longitud_encerrojado', models.FloatField(default=6000)),
                ('longitud_total', models.FloatField(default=36000)),
                ('fecha_aprovacion', models.DateField()),
                ('fecha_certificacion', models.DateField()),
                ('aprovador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.aprovador')),
                ('certificador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.certificador')),
                ('diseñador', models.ForeignKey(limit_choices_to={'de_cambiadores': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.diseñador')),
                ('fabricante', models.ForeignKey(limit_choices_to={'de_cambiadores': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.fabricante')),
            ],
        ),
        migrations.CreateModel(
            name='Vagon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=16, unique=True)),
                ('tipo', models.CharField(default=' ', max_length=20)),
                ('descripcion', models.CharField(default=' ', max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='vagones/')),
                ('lng', models.FloatField(default=-3.982)),
                ('lat', models.FloatField(default=40.2951)),
                ('composicion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.composicion')),
                ('keeper', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.keeper')),
                ('mantenedor', models.ForeignKey(limit_choices_to={'de_vagones': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.mantenedor')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.operador')),
            ],
        ),
        migrations.AddField(
            model_name='operador',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.AddField(
            model_name='mantenedor',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.AddField(
            model_name='keeper',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.AddField(
            model_name='fabricante',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.CreateModel(
            name='Eje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('fecha_fab', models.DateField(auto_now_add=True)),
                ('num_cambios', models.IntegerField(default=0)),
                ('km', models.FloatField(default=0)),
                ('mantenimiento', models.CharField(max_length=16)),
                ('coef_trabajo', models.FloatField(default=0)),
                ('alarmas_cambio', models.IntegerField(default=0)),
                ('alarmas_circulacion', models.IntegerField(default=0)),
                ('lng', models.FloatField(default=-3.982)),
                ('lat', models.FloatField(default=40.2951)),
                ('fabricante', models.ForeignKey(limit_choices_to={'de_ejes': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.fabricante')),
                ('keeper', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.keeper')),
                ('mantenedor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.mantenedor')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.operador')),
                ('vagon', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.vagon')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.versioneje')),
            ],
        ),
        migrations.AddField(
            model_name='diseñador',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.AddField(
            model_name='composicion',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.operador'),
        ),
        migrations.CreateModel(
            name='Circulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_inicio', models.CharField(max_length=30)),
                ('loc_final', models.CharField(max_length=30)),
                ('dia', models.DateField()),
                ('Vmed', models.FloatField(default=2.77)),
                ('km', models.FloatField(default=340)),
                ('alarmas', models.BooleanField(default=False)),
                ('eje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.eje')),
            ],
        ),
        migrations.AddField(
            model_name='certificador',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.CreateModel(
            name='Cambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cambio_eje', models.IntegerField(default=0)),
                ('alarma', models.BooleanField(default=False)),
                ('inicio', models.DateTimeField()),
                ('sentido', models.CharField(choices=[('UICIB', 'UIC->IB'), ('IBUIC', 'IB->UIC'), ('UICRUS', 'UIC->RUS'), ('RUSUIC', 'RUS->UIC')], default='UICIB', max_length=8)),
                ('V', models.FloatField(default=2.77)),
                ('FV', models.FloatField(default=250)),
                ('tdaM', models.FloatField(default=5000)),
                ('fdaM', models.FloatField(default=30)),
                ('ddaM', models.FloatField(default=10)),
                ('tcaM', models.FloatField(default=10000)),
                ('fcaM', models.FloatField(default=20)),
                ('dcaM', models.FloatField(default=70)),
                ('team', models.FloatField(default=15000)),
                ('feam', models.FloatField(default=10)),
                ('deam', models.FloatField(default=20)),
                ('tdbM', models.FloatField(default=25000)),
                ('fdbM', models.FloatField(default=30)),
                ('ddbM', models.FloatField(default=10)),
                ('tcbM', models.FloatField(default=300000)),
                ('fcbM', models.FloatField(default=20)),
                ('dcbM', models.FloatField(default=70)),
                ('tebm', models.FloatField(default=35000)),
                ('febm', models.FloatField(default=10)),
                ('debm', models.FloatField(default=20)),
                ('cambiador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.cambiador')),
                ('eje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.eje')),
            ],
        ),
        migrations.AddField(
            model_name='cambiador',
            name='fabricante',
            field=models.ForeignKey(limit_choices_to={'de_cambiadores': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.fabricante'),
        ),
        migrations.AddField(
            model_name='cambiador',
            name='mantenedor',
            field=models.ForeignKey(limit_choices_to={'de_cambiadores': True}, on_delete=django.db.models.deletion.RESTRICT, to='mercave.mantenedor'),
        ),
        migrations.AddField(
            model_name='cambiador',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='mercave.versioncambiador'),
        ),
        migrations.AddField(
            model_name='aprovador',
            name='organizacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.organizacion'),
        ),
        migrations.CreateModel(
            name='AlarmaCirculacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('mensaje', models.CharField(max_length=30)),
                ('vista', models.BooleanField(default=False)),
                ('ax0', models.FloatField(default=2.77)),
                ('ay0', models.FloatField(default=2.77)),
                ('az0', models.FloatField(default=2.77)),
                ('t0', models.FloatField(default=2.77)),
                ('ax1', models.FloatField(default=2.77)),
                ('ay1', models.FloatField(default=2.77)),
                ('az1', models.FloatField(default=2.77)),
                ('t1', models.FloatField(default=2.77)),
                ('ax2', models.FloatField(default=2.77)),
                ('ay2', models.FloatField(default=2.77)),
                ('az2', models.FloatField(default=2.77)),
                ('t2', models.FloatField(default=2.77)),
                ('ax3', models.FloatField(default=2.77)),
                ('ay3', models.FloatField(default=2.77)),
                ('az3', models.FloatField(default=2.77)),
                ('t3', models.FloatField(default=2.77)),
                ('ax4', models.FloatField(default=2.77)),
                ('ay4', models.FloatField(default=2.77)),
                ('az4', models.FloatField(default=2.77)),
                ('t4', models.FloatField(default=2.77)),
                ('ax5', models.FloatField(default=2.77)),
                ('ay5', models.FloatField(default=2.77)),
                ('az5', models.FloatField(default=2.77)),
                ('t5', models.FloatField(default=2.77)),
                ('ax6', models.FloatField(default=2.77)),
                ('ay6', models.FloatField(default=2.77)),
                ('az6', models.FloatField(default=2.77)),
                ('t6', models.FloatField(default=2.77)),
                ('ax7', models.FloatField(default=2.77)),
                ('ay7', models.FloatField(default=2.77)),
                ('az7', models.FloatField(default=2.77)),
                ('t7', models.FloatField(default=2.77)),
                ('ax8', models.FloatField(default=2.77)),
                ('ay8', models.FloatField(default=2.77)),
                ('az8', models.FloatField(default=2.77)),
                ('t8', models.FloatField(default=2.77)),
                ('ax9', models.FloatField(default=2.77)),
                ('ay9', models.FloatField(default=2.77)),
                ('az9', models.FloatField(default=2.77)),
                ('t9', models.FloatField(default=2.77)),
                ('circulacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.circulacion')),
            ],
        ),
        migrations.CreateModel(
            name='AlarmaCambio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=30)),
                ('vista', models.BooleanField(default=False)),
                ('cambio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mercave.cambio')),
            ],
        ),
    ]
