from lib.mmonit import MmonitBaseAction


class MmonitGetStatusHost(MmonitBaseAction):
    def run(self, host_id):
        self.login()
        data = {"id": host_id}
        req = self.session.get("{}/admin/hosts/get".format(self.url), params=data)

        try:
            return req.json()
        except Exception as error:
            return error.message
        finally:
            self.logout()