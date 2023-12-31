from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Menu title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Menu slug')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='MenuItem title')),
                ('slug', models.SlugField(max_length=255, verbose_name='MenuItem slug')),
                ('menu', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tree_menu.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='tree_menu.menuitem')),
            ],
            options={
                'verbose_name': 'MenuItem',
                'verbose_name_plural': 'MenuItems',
            },
        ),
    ]