# Generated by Django 2.2.7 on 2019-11-18 11:34

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('industry', models.CharField(choices=[('Energy', (('101010', 'Energy Equipment & Services'), ('101020', 'Oil, Gas & Consumable Fuels'))), ('Materials', (('151010', 'Chemicals'), ('151020', 'Construction Materials'), ('151030', 'Containers & Packaging'), ('151040', 'Metals & Mining'), ('151050', 'Paper & Forest Products'))), ('Capital Goods', (('201010', 'Aerospace & Defense'), ('201020', 'Building Products'), ('201030', 'Construction & Engineering'), ('201040', 'Electrical Equipment'), ('201050', 'Industrial Conglomerates'), ('201060', 'Machinery'), ('201070', 'Trading Companies & Distributors'))), ('Commercial & Professional Services', (('202010', 'Commercial Services & Supplies'), ('202020', 'Professional Services'))), ('Transportation', (('203010', 'Air Freight & Logistics'), ('203020', 'Airlines'), ('203030', 'Marine'), ('203040', 'Road & Rail'), ('203050', 'Transportation Infrastructure'))), ('Automobiles & Components', (('251010', 'Auto Components'), ('251020', 'Automobiles'))), ('Consumer Durables & Apparel', (('252010', 'Household Durables'), ('252020', 'Leisure Products'), ('252030', 'Textiles, Apparel & Luxury Goods'))), ('Consumer Services', (('253010', 'Hotels, Restaurants & Leisure'), ('253020', 'Diversified Consumer Services'))), ('Media', (('254010', 'Media'),)), ('Retailing', (('255010', 'Distributors'), ('255020', 'Internet & Catalog Retail'), ('255030', 'Multiline Retail'), ('255040', 'Specialty Retail'))), ('Food & Staples Retailing', (('301010', 'Food & Staples Retailing'),)), ('Food, Beverage & Tobacco', (('302010', 'Beverages'), ('302020', 'Food Products'), ('302030', 'Tobacco'))), ('Household & Personal Products', (('303010', 'Household Products'), ('303020', 'Personal Products'))), ('Health Care Equipment & Services', (('351010', 'Health Care Equipment & Supplies'), ('351020', 'Health Care Providers & Services'), ('351030', 'Health Care Technology'))), ('Pharmaceuticals, Biotechnology & Life Sciences', (('352010', 'Biotechnology'), ('352020', 'Pharmaceuticals'), ('352030', 'Life Sciences Tools & Services'))), ('Banks', (('401010', 'Banks'), ('401020', 'Thrifts & Mortgage Finance'))), ('Diversified Financials', (('402010', 'Diversified Financial Services'), ('402020', 'Consumer Finance'), ('402030', 'Capital Markets'))), ('Insurance', (('403010', 'Insurance'),)), ('Real Estate', (('404020', 'Real Estate Investment Trusts (REITs)'), ('404030', 'Real Estate Management & Development'))), ('Software & Services', (('451010', 'Internet Software & Services'), ('451020', 'IT Services'), ('451030', 'Software'))), ('Technology Hardware & Equipment', (('452010', 'Communications Equipment'), ('452020', 'Technology Hardware, Storage & Peripherals'), ('452030', 'Electronic Equipment, Instruments & Components'))), ('Semiconductors & Semiconductor Equipment', (('453010', 'Semiconductors & Semiconductor Equipment'),)), ('Telecommunication Services', (('501010', 'Diversified Telecommunication Services'), ('501020', 'Wireless Telecommunication Services'))), ('Utilities', (('551010', 'Electric Utilities'), ('551020', 'Gas Utilities'), ('551030', 'Multi-Utilities'), ('551040', 'Water Utilities'), ('551050', 'Independent Power and Renewable Electricity Producers')))], max_length=6)),
                ('ceo', models.CharField(blank=True, default='', max_length=100)),
                ('website', models.URLField(max_length=100)),
                ('image', models.ImageField(upload_to='companies')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial_statements', to='companies.Company')),
            ],
        ),
        migrations.AddConstraint(
            model_name='financialstatement',
            constraint=models.UniqueConstraint(fields=('company', 'date'), name='unique_company_financial_statement'),
        ),
    ]