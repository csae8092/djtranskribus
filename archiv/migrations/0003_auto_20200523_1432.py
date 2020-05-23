# Generated by Django 3.0.6 on 2020-05-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archiv', '0002_auto_20200523_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trpcollection',
            name='image_url',
            field=models.CharField(blank=True, help_text='Image URL', max_length=250, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='trpcollection',
            name='name',
            field=models.CharField(blank=True, help_text='Collection Name', max_length=250, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='trpcollection',
            name='role',
            field=models.CharField(blank=True, help_text='Role', max_length=250, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='trpcollection',
            name='thumb_url',
            field=models.CharField(blank=True, help_text='Thumb URL', max_length=250, null=True, verbose_name='Thumb URL'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='author',
            field=models.CharField(blank=True, help_text='Author of the Document', max_length=250, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='authority',
            field=models.CharField(blank=True, help_text='Authority', max_length=250, null=True, verbose_name='Authority'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='external_id',
            field=models.CharField(blank=True, help_text='External ID', max_length=250, null=True, verbose_name='External ID'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='genre',
            field=models.CharField(blank=True, help_text='Genre', max_length=250, null=True, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='image_url',
            field=models.CharField(blank=True, help_text='Image URL', max_length=250, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='language',
            field=models.CharField(blank=True, help_text='Language of the Document', max_length=250, null=True, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='script_type',
            field=models.CharField(blank=True, help_text='Script Type', max_length=250, null=True, verbose_name='Script Type'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='thumb_url',
            field=models.CharField(blank=True, help_text='Thumb URL', max_length=250, null=True, verbose_name='Thumb URL'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='uploader',
            field=models.CharField(blank=True, help_text='Uploader Email', max_length=250, null=True, verbose_name='Uploader (email)'),
        ),
        migrations.AlterField(
            model_name='trpdocument',
            name='writer',
            field=models.CharField(blank=True, help_text='Writer/Hand', max_length=250, null=True, verbose_name='Writer'),
        ),
        migrations.AlterField(
            model_name='trppage',
            name='img_file_name',
            field=models.CharField(blank=True, help_text='Filename', max_length=250, null=True, verbose_name='Filename'),
        ),
        migrations.AlterField(
            model_name='trppage',
            name='page_key',
            field=models.CharField(blank=True, help_text='Key of the Page', max_length=250, null=True, verbose_name='Key of the Page'),
        ),
        migrations.AlterField(
            model_name='trppage',
            name='page_url',
            field=models.CharField(blank=True, help_text='URL of Image', max_length=250, null=True, verbose_name='URL of Image'),
        ),
        migrations.AlterField(
            model_name='trppage',
            name='thum_url',
            field=models.CharField(blank=True, help_text='Thumb URL', max_length=250, null=True, verbose_name='Thumb URL'),
        ),
        migrations.AlterField(
            model_name='trptranscript',
            name='status',
            field=models.CharField(blank=True, help_text='status', max_length=250, null=True, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='trptranscript',
            name='transcriber',
            field=models.CharField(blank=True, help_text='Transcriber (email)', max_length=250, null=True, verbose_name='Transcriber (email)'),
        ),
        migrations.AlterField(
            model_name='trptranscript',
            name='transcript_key',
            field=models.CharField(blank=True, help_text='Key of Transcript', max_length=250, null=True, verbose_name='Key of Transcript'),
        ),
        migrations.AlterField(
            model_name='trptranscript',
            name='transcript_url',
            field=models.CharField(blank=True, help_text='Url of Transcript', max_length=250, null=True, verbose_name='Url of Transcript'),
        ),
    ]