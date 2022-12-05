/*
Copyright: SCLE SFE
Contributor: Julien Pagès <j.parkouss@gmail.com>

This software is a computer program whose purpose is to test graphical
applications written with the QT framework (http://qt.digia.com/).

This software is governed by the CeCILL v2.1 license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL v2.1 license and that you accept its terms.
*/

#ifndef FUNQ_H
#define FUNQ_H

#include <QHostAddress>
#include <QObject>

class QTcpServer;
class Pick;

class Funq : public QObject {
    Q_OBJECT
public:
    static void activate(bool check_activation = false);

    enum MODE { PLAYER, PICK };

protected:
    explicit Funq(MODE mode, const QHostAddress & host, int port);
    bool eventFilter(QObject * receiver, QEvent * event);

signals:

private slots:
    void onNewConnection();
    void funqInit();

private:
    static bool registerPick();
    static bool unRegisterPick();
    static bool hook(void ** data);
    static void active_hook_player(MODE mode);

    static Funq * _instance;

    MODE m_mode;
    int m_port;
    QHostAddress m_host;
    QTcpServer * m_server;
    Pick * m_pick;
};

#endif  // FUNQ_H
