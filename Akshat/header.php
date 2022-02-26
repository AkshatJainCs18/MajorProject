<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>

            </button>
                <h3 href="index.php" class="navbar-brand">Medico Predict</h3>
          </div>
            <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav navbar-right">
                <?php 
                if(isset($_SESSION['email']))
                {?>
                <li><a href="logout.php"><span class="glyphicon glyphicon-log-out"> Logout</span></a></li>
                <?php }
                else {?>
                   <li><a href="login.php"><span class="glyphicon glyphicon-log-in"> Login</span></a></li>
                <li><a href="signup.php"><span class="glyphicon glyphicon-user"> Signup</span></a></li>
                <?php } ?>
            </ul>
           </div> 
         </div>

        </div>

    </div>
</nav>