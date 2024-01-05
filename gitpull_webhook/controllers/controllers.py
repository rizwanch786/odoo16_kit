from odoo import http
from odoo.http import request
from subprocess import Popen, PIPE
import hmac
import hashlib


class GitHubWebhook(http.Controller):
    @http.route('/webhook-endpoint', type='http', auth='none', methods=['GET', 'POST'], csrf=False)
    def handle_webhook(self, **post):
        if request.httprequest.method == 'POST':
            secret_token = 'a36c62b04d6ffcb7dc8d628fee26e33694e8684c'
            signature = request.httprequest.headers.get('X-Hub-Signature')
            payload = request.httprequest.data

            if not self._verify_signature(payload, secret_token, signature):
                return http.Response('Invalid Signature', status=403)

            self._pull_changes()
            return http.Response('Webhook received successfully', status=200)

        elif request.httprequest.method == 'GET':
            # Your existing GET handling logic here (if needed)
            return http.Response('GET request received', status=200)

    def _verify_signature(self, payload, secret, signature):
        if not secret or not signature:
            return False

        sha_name, signature = signature.split('=')
        mac = hmac.new(secret.encode('utf-8'), msg=payload, digestmod=hashlib.sha1)
        return hmac.compare_digest(mac.hexdigest(), signature)

    def _pull_changes(self):
        repo_url = 'https://github.com/rizwanch786/odoo16_kit.git'
        branch = 'main'
        addons_path = '/opt/odoo16kit/odoo-custom-addons/odoo16_kit'

        cmd = ['git', 'pull', '--force', '--recurse-submodules', repo_url, branch]
        process = Popen(cmd, cwd=addons_path, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            self._log_info(f'Successfully pulled changes from {repo_url}/{branch}')
        else:
            self._log_error(f'Error pulling changes: {stderr.decode("utf-8")}')

    def _log_info(self, message):
        # Replace this with your preferred logging mechanism
        print(f'INFO: {message}')

    def _log_error(self, message):
        # Replace this with your preferred logging mechanism
        print(f'ERROR: {message}')
