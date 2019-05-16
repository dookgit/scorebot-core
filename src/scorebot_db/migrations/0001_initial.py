# Generated by Django 2.1 on 2018-08-12 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import scorebot.util
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exclude', models.BooleanField(default=True, verbose_name='Monitor Exclude')),
            ],
            options={
                'verbose_name': '[Game] Assigned Monitor',
                'verbose_name_plural': '[Game] Assigned Monitors',
            },
        ),
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.BigIntegerField(default=0, verbose_name='Access Boolean Byte')),
            ],
            options={
                'verbose_name': '[Access] Access Token',
                'verbose_name_plural': '[Access] Access Tokens',
            },
        ),
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Beacon Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Beacon Finish')),
                ('scored', models.DateTimeField(editable=False, null=True, verbose_name='Beacon Last Scored')),
            ],
            options={
                'verbose_name': '[Range] Beacon',
                'verbose_name_plural': '[Range] Beacons',
            },
        ),
        migrations.CreateModel(
            name='BeaconHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unpack_ipv4=True, verbose_name='Beacon Host Address')),
            ],
            options={
                'verbose_name': '[Range] Beacon Host',
                'verbose_name_plural': '[Range] Beacon Hosts',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=64, verbose_name='Content Format')),
                ('data', models.TextField(blank=True, null=True, verbose_name='Content Data')),
                ('value', models.PositiveSmallIntegerField(default=100, verbose_name='Content Score Value')),
            ],
            options={
                'verbose_name': '[Range] Service Content',
                'verbose_name_plural': '[Range] Service Content',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=75, verbose_name='Credit Name')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Credit HTML Code')),
            ],
            options={
                'verbose_name': '[Game] Credit',
                'verbose_name_plural': '[Game] Credits',
            },
        ),
        migrations.CreateModel(
            name='DNS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unpack_ipv4=True, verbose_name='DNS Server Address')),
            ],
            options={
                'verbose_name': '[Range] DNS Server',
                'verbose_name_plural': '[Range] DNS Servers',
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=64, verbose_name='Flag Name')),
                ('flag', models.CharField(max_length=128, verbose_name='Flag Value')),
                ('enabled', models.BooleanField(default=True, verbose_name='Flag Enabled')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Flag Description')),
                ('value', models.PositiveSmallIntegerField(default=100, verbose_name='Flag Score Value')),
            ],
            options={
                'verbose_name': '[Range] Flag',
                'verbose_name_plural': '[Range] Flags',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Game Name')),
                ('start', models.DateTimeField(null=True, verbose_name='Game Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Game Finish')),
                ('mode', models.PositiveIntegerField(choices=[(0, 'Red vs Blue'), (1, 'Blue vs Blue'), (2, 'King'), (3, 'High Ground')], default=0, verbose_name='Game Mode')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Stopped'), (1, 'Running'), (3, 'Paused'), (4, 'Completed'), (5, 'Archived')], default=0, verbose_name='Game Status')),
            ],
            options={
                'verbose_name': '[Game] Game',
                'verbose_name_plural': '[Game] Games',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='Host Enabled')),
                ('name', models.SlugField(max_length=64, null=True, verbose_name='Host Nickname')),
                ('status', models.BooleanField(default=False, editable=False, verbose_name='Host Online')),
                ('scored', models.DateTimeField(editable=False, null=True, verbose_name='Host Last Scored')),
                ('fqdn', models.CharField(blank=True, max_length=128, null=True, verbose_name='Host Full Name')),
                ('value', models.PositiveSmallIntegerField(default=100, verbose_name='Host Score Value')),
                ('ip', models.GenericIPAddressField(unpack_ipv4=True, verbose_name='Host Address')),
                ('tolerance', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Host Ping Tolerance Percentage')),
            ],
            options={
                'verbose_name': '[Range] Host',
                'verbose_name_plural': '[Range] Hosts',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '[Store] Item',
                'verbose_name_plural': '[Store] Items',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Job Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Job Finish')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='scorebot_db.Host')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='scorebot_db.AssignedMonitor')),
            ],
            options={
                'verbose_name': '[Game] Job',
                'verbose_name_plural': '[Game] Jobs',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Member Name')),
                ('score', models.BigIntegerField(default=0, verbose_name='Member Lifetime Score')),
                ('handle', models.CharField(blank=True, max_length=64, null=True, verbose_name='Member Twitter Handle')),
            ],
            options={
                'verbose_name': '[Player] Member',
                'verbose_name_plural': '[Player] Members',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Membership Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Membership Logo')),
                ('score', models.BigIntegerField(default=0, verbose_name='Membership Lifetime Score')),
                ('color', models.CharField(default='#306d4f', max_length=9, verbose_name='Membership Color')),
            ],
            options={
                'verbose_name': '[Player] Membership',
                'verbose_name_plural': '[Player] Memberships',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=75, verbose_name='Monitor Name')),
                ('token', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_db.Authorization')),
            ],
            options={
                'verbose_name': '[Game] Monitor',
                'verbose_name_plural': '[Game] Monitors',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Player Name')),
                ('score', models.IntegerField(default=0, editable=False, verbose_name='Player Score')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='scorebot_db.Member')),
            ],
            options={
                'verbose_name': '[Player] Player',
                'verbose_name_plural': '[Player] Players',
            },
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.PositiveIntegerField(verbose_name='Beacon Port')),
            ],
            options={
                'verbose_name': '[Game] Beacon Port',
                'verbose_name_plural': '[Game] Beacon Ports',
            },
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=64, verbose_name='Range Domain')),
                ('subnet', models.CharField(max_length=128, verbose_name='Range Subnet')),
                ('enabled', models.BooleanField(default=True, verbose_name='Range Enabled')),
                ('dns', models.ManyToManyField(related_name='ranges', to='scorebot_db.DNS')),
            ],
            options={
                'verbose_name': '[Range] Range',
                'verbose_name_plural': '[Range] Ranges',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name='Service Port')),
                ('bonus', models.BooleanField(default=False, verbose_name='Service is Bonus')),
                ('enabled', models.BooleanField(default=True, verbose_name='Service Enabled')),
                ('name', models.SlugField(max_length=64, null=True, verbose_name='Service Name')),
                ('value', models.PositiveSmallIntegerField(default=100, verbose_name='Service Score Value')),
                ('bonus_enabled', models.BooleanField(default=False, editable=False, verbose_name='Service Bonus Enabled')),
                ('application', models.SlugField(blank=True, max_length=64, null=True, verbose_name='Service Application')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'red'), (1, 'yellow'), (2, 'green')], default=0, verbose_name='Service Status')),
                ('protocol', models.PositiveSmallIntegerField(choices=[(0, 'tcp'), (1, 'udp'), (2, 'icmp')], default=0, verbose_name='Service Protocol')),
                ('content', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_db.Content')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='scorebot_db.Host')),
            ],
            options={
                'verbose_name': '[Range] Service',
                'verbose_name_plural': '[Range] Services',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=150, verbose_name='Settings Name')),
                ('beacon_score', models.PositiveSmallIntegerField(default=300, verbose_name='Beacon Scoring Value')),
                ('beacon_time', models.PositiveSmallIntegerField(default=300, verbose_name='Beacon Timeout (seconds)')),
                ('job_timeout', models.PositiveSmallIntegerField(default=300, verbose_name='Unfinished Job Timeout (seconds)')),
                ('host_ping', models.PositiveSmallIntegerField(default=100, verbose_name='General Host Ping Tolerance Percentage')),
                ('job_cleanup_time', models.PositiveSmallIntegerField(default=900, verbose_name='Finished Job Cleanup Time (seconds)')),
            ],
            options={
                'verbose_name': '[Game] Game Settings',
                'verbose_name_plural': '[Game] Game Settings',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '[Store] Storefront',
                'verbose_name_plural': '[Store] Storefronts',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Team Name')),
                ('subclass', models.PositiveSmallIntegerField(choices=[(0, 'Team'), (1, 'ScoreTeam'), (2, 'PlayerTeam')], default=None, editable=False, null=True, verbose_name='Team SubClass')),
            ],
            options={
                'verbose_name': '[Team] Team',
                'verbose_name_plural': '[Team] Teams',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('expires', models.DateTimeField(blank=True, null=True, verbose_name='Token Expire Time')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Token UUID')),
            ],
            options={
                'verbose_name': '[Access] Authentication Token',
                'verbose_name_plural': '[Access] Authentication Tokens',
                'get_latest_by': 'expires',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='Transaction Value')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='Transaction Date/Time')),
                ('subclass', models.PositiveSmallIntegerField(choices=[(0, 'Transaction'), (1, 'Payment'), (2, 'Transfer'), (3, 'Purchase'), (4, 'Correction'), (5, 'PaymentHealth'), (6, 'TransferResult'), (7, 'TransactionFlag'), (8, 'TransactionBeacon')], default=None, editable=False, null=True, verbose_name='Team SubClass')),
            ],
            options={
                'verbose_name': '[Score] Transaction',
                'verbose_name_plural': '[Score] Transaction',
            },
        ),
        migrations.CreateModel(
            name='Correction',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
                ('reason', models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'Scoring Error'), (2, 'Invalid Score Issued')], default=0, verbose_name='Correction Reason')),
            ],
            options={
                'verbose_name': '[Score] Correction',
                'verbose_name_plural': '[Score] Correction',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
            ],
            options={
                'verbose_name': '[Score] Payment',
                'verbose_name_plural': '[Score] Payments',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='PaymentHealth',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
                ('expected', models.IntegerField(verbose_name='Expected Payment Value')),
            ],
            options={
                'verbose_name': '[Score] Health Payment',
                'verbose_name_plural': '[Score] Health Payments',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchases', to='scorebot_db.Item')),
            ],
            options={
                'verbose_name': '[Score] Purchase',
                'verbose_name_plural': '[Score] Purchases',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='ScoreTeam',
            fields=[
                ('team_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Team')),
                ('total', models.BigIntegerField(default=0, editable=False, verbose_name='Team Total Score')),
            ],
            options={
                'verbose_name': '[Team] Score Team',
                'verbose_name_plural': '[Team] Score Teams',
            },
            bases=('scorebot_db.team',),
        ),
        migrations.CreateModel(
            name='TransactionBeacon',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
            ],
            options={
                'verbose_name': '[Score] Beacon Transaction',
                'verbose_name_plural': '[Score] Beacon Transactions',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='TransactionFlag',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
            ],
            options={
                'verbose_name': '[Score] Flag Transaction',
                'verbose_name_plural': '[Score] Flag Transactions',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
                ('processed', models.BooleanField(default=False, verbose_name='Tranfer Processed')),
                ('approved', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Tansfer Approved')),
            ],
            options={
                'verbose_name': '[Score] Transfer',
                'verbose_name_plural': '[Score] Transfer',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.CreateModel(
            name='TransferResult',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.Transaction')),
            ],
            options={
                'verbose_name': '[Score] Transfer Result',
                'verbose_name_plural': '[Score] Transfer Result',
            },
            bases=('scorebot_db.transaction',),
        ),
        migrations.AddField(
            model_name='transaction',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='scorebot_db.Team'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_db.Transaction'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payer', to='scorebot_db.Team'),
        ),
        migrations.AddField(
            model_name='team',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='scorebot_db.Game'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='scorebot_db.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_db.Token'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='scorebot_db.Membership'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='host',
            name='range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='scorebot_db.Range'),
        ),
        migrations.AddField(
            model_name='game',
            name='ports',
            field=models.ManyToManyField(blank=True, to='scorebot_db.Port'),
        ),
        migrations.AddField(
            model_name='game',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='scorebot_db.Settings'),
        ),
        migrations.AddField(
            model_name='flag',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='scorebot_db.Host'),
        ),
        migrations.AddField(
            model_name='beaconhost',
            name='range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ghosts', to='scorebot_db.Range'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='ghost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beacons', to='scorebot_db.BeaconHost'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='host',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beacons', to='scorebot_db.Host'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beacons', to='scorebot_db.Token'),
        ),
        migrations.AddField(
            model_name='authorization',
            name='token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='keys', to='scorebot_db.Token'),
        ),
        migrations.AddField(
            model_name='assignedmonitor',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitors', to='scorebot_db.Game'),
        ),
        migrations.AddField(
            model_name='assignedmonitor',
            name='monitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='scorebot_db.Monitor'),
        ),
        migrations.AddField(
            model_name='assignedmonitor',
            name='selected',
            field=models.ManyToManyField(blank=True, to='scorebot_db.Host'),
        ),
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('scoreteam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scorebot_db.ScoreTeam')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Team Logo')),
                ('offensive', models.BooleanField(default=False, verbose_name='Team Can Attack')),
                ('minimal', models.BooleanField(default=False, verbose_name='Team Score Is Hidden')),
                ('color', models.CharField(default=scorebot.util.hex_color, max_length=9, verbose_name='Team Color')),
                ('store', models.PositiveIntegerField(blank=True, null=True, verbose_name='Team Store ID')),
                ('deduction', models.PositiveSmallIntegerField(default=0, verbose_name='Team Score Deduction Percentage')),
                ('membership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='scorebot_db.Membership')),
                ('registered', models.ManyToManyField(blank=True, related_name='beacon_tokens', to='scorebot_db.Token')),
            ],
            options={
                'verbose_name': '[Team] Player Team',
                'verbose_name_plural': '[Team] Player Teams',
            },
            bases=('scorebot_db.scoreteam',),
        ),
        migrations.AddField(
            model_name='transactionflag',
            name='flag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='scorebot_db.Flag'),
        ),
        migrations.AddField(
            model_name='transactionbeacon',
            name='beacon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='scorebot_db.Beacon'),
        ),
        migrations.AddField(
            model_name='scoreteam',
            name='stack',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='scorebot_db.Transaction'),
        ),
        migrations.AddField(
            model_name='scoreteam',
            name='token',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_db.Token'),
        ),
        migrations.AddField(
            model_name='range',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ranges', to='scorebot_db.PlayerTeam'),
        ),
        migrations.AddField(
            model_name='payment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='scorebot_db.PlayerTeam'),
        ),
        migrations.AddField(
            model_name='flag',
            name='stolen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='captured', to='scorebot_db.PlayerTeam'),
        ),
        migrations.AddField(
            model_name='beacon',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beacons', to='scorebot_db.PlayerTeam'),
        ),
    ]
