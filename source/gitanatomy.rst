Anatomy of Git repositories
===========================

Merkle tree
-----------

.. graphviz::

   digraph {
      nodesep = 1.5
      node [ shape = component, fontname = "monospace" ]
      edge [ fontname = "monospace", labelfontname = "monospace" ]
      blob1 [ shape = note, label = "9daeafb", tooltip = "9daeafb9864cf43055ae93beb0afd6c7d144bfa4" ]
      blob2 [ shape = note, label = "3e75765" ]
      blob3 [ shape = note, label = "180cf83" ]
      blob4 [ shape = note, label = "a5bce3f" ]
      subblob [ shape = note, label = "e69de29" ]
      tree1 [ shape = folder, label = "ae5c731" ]
      tree2 [ shape = folder, label = "bffa072" ]
      subtree [ shape = folder, label = "c5a917c" ]

      tree1 -> blob1 [ arrowhead = diamond, label = "file.dat", constraint = false ]
      tree1 -> blob2 [ arrowhead = diamond, label = "newfile.dat" ]
      tree2 -> blob1 [ arrowhead = diamond, label = "file.dat", constraint = false ]
      tree2 -> blob3 [ arrowhead = diamond, label = "oldname.dat" ]
      tree1 -> blob3 [ arrowhead = diamond, label = "newname.dat" ]
      tree2 -> blob4 [ arrowhead = diamond, label = "deleted.dat" ]
      subtree -> subblob [ arrowhead = diamond, label = "subfile.dat" ]
      tree1 -> subtree [ arrowhead = diamond, label = "dir/", minlen = 2 ]
      tree2 -> subtree [ arrowhead = diamond, label = "dir/" ]

      commit1 [ tooltip = "git mv oldname.dat newname.dat\ngit rm deleted.dat\ngit add newfile.dat", fontsize = 12,
                label = "5ecdca016974fe5faa884c24515f3e6302209d7e\l\lAuthor: John R. Hacker <jrhacker@example.com>\lDate: Fri Mar 10 18:45:22 2023 +0300\l\llatest commit here\l"]
      commit4 [ label = "92d8745\linitial commit" ]
      commit3 [ label = "7b81d07" ]
      commit2 [ label = "eb04ee5" ]
      commit6 [ label = "fa3f8af" ]
      commit5 [ label = "0941846" ]
      commit1 -> tree1
      commit2 -> tree2
      commit1 -> commit2
      commit2 -> commit3
      commit3 -> commit4
      commit5 -> commit6
      commit6 -> commit3
      head [ shape = point, xlabel = "HEAD", fontname = "monospace" ]
      head -> commit1
      branch1 [ shape = invhouse, label = "devel" ]
      branch1 -> commit5
      branch2 [ shape = invhouse, label = "stable" ]
      branch2 -> commit1
      tag1 [ shape = cds, label = "v1.0.0" ]
      tag1 -> commit3

      commit2 -> blob1 [ style = invis ]
   }

.. graphviz::

   digraph {
     bgcolor = lightgray
     pad = 0.5
     node [ fontname = "times-italic" ]
     ex_blob [ shape = note, label = "Blob object" ]
     ex_tree [ shape = folder, label = "Tree object" ]
     ex_commit [ shape = component, label = "Commit object" ]
     ex_tag [ shape = cds, label = "Tag (object)" ]
     ex_branch [ shape = invhouse, label = "Branch" ]
     ex_head [ shape = point, xlabel = "Head" ]

     ex_objects [ shape = none, label = "Objects", fontname = "serif" ]
     ex_refs [ shape = none, label = "References",  fontname = "serif"  ]

     ex_blob -> ex_objects [ dir = none ]
     ex_tree -> ex_objects [ dir = none ]
     ex_commit -> ex_objects [ dir = none ]
     ex_tag -> ex_objects [ dir = none ]
     ex_tag -> ex_refs [ dir = none ]
     ex_branch -> ex_refs [ dir = none ]
     ex_head -> ex_refs [ dir = none ]
   }

+----------+----------+--------+
| Ref      | Tracking | Global |
+==========+==========+========+
| HEAD     | Yes      | No     |
+----------+----------+--------+
| tags     | No       | Yes/No |
+----------+----------+--------+
| branches | Yes      | Yes    |
+----------+----------+--------+


Immutability
------------

.. graphviz::

   digraph {
      node [ shape = component, fontname = "monospace" ]
      edge [ fontname = "monospace", labelfontname = "monospace" ]
      compound = true
      rankdir = LR

      subgraph cluster_old {
          branch [ shape = invhouse, label = "stable" ]
          head [ shape = point, xlabel = "HEAD" ]
          tag [ shape = cds, label = "v1.0.1" ]
          commit1 [ label = "5ecdca0" ]
          commit2 [ label = "eb04ee5" ]
      }

      subgraph cluster_new {
          brancha [  shape = invhouse, label = "stable" ]
          heada [ shape = point, xlabel = "HEAD" ]
          taga [ shape = cds, label = "v1.0.1", color = gray, fontcolor = gray ]
          commit1a [ label = "5ecdca0", color = gray, fontcolor = gray ]
          commit2a [ label = "eb04ee5", color = gray, fontcolor = gray ]
          commit1prime [ label = "1de5a69" ]
      }

      subgraph cluster_reset {
          branchb [  shape = invhouse, label = "stable" ]
          headb [ shape = point, xlabel = "HEAD" ]
          tagb [ shape = cds, label = "v1.0.1" ]
          commit1b [ label = "5ecdca0" ]
          commit2b [ label = "eb04ee5" ]
          commit1orphan [ label = "1de5a69", fontcolor = lightgray, color = lightgray ]
      }

      commit1 -> commit2
      branch -> commit1
      head -> commit1
      tag -> commit1

      commit1a -> commit2a [ color = gray ]
      commit1prime -> commit2a

      brancha -> commit1prime
      heada -> commit1prime
      taga -> commit1a [ color = gray ]

      command [ label = "git commit --amend", shape = rarrow ]
      commit1 -> command [ style = invis ]
      command -> commit1prime [ style = invis ]

      commit1b -> commit2b
      commit1orphan -> commit2b
      branchb -> commit1b
      headb -> commit1b
      tagb -> commit1b

      command2 [ label = "git reset --hard v1.0.1", shape = rarrow ]
      commit1prime -> command2 [ style = invis ]
      command2 -> commit1b [ style = invis ]
   }

Distributed repositories
------------------------

Basic push
++++++++++

.. graphviz::

   digraph {
      subgraph cluster_baserepo {
         label = "Remote repo"
         base_commit [ shape = component, label = "Base commit" ]
         origin_branch [ shape = invhouse,  label = "origin/branch", fontname = "monospace" ]
         commit2_base  [ shape = component, label = "Commit 2" ]
         origin_branch_new [ shape = invhouse, label = "origin/branch", fontname = "monospace" ]

         origin_branch -> base_commit [ constraint = false ]
         origin_branch_new -> commit2_base [ constraint = false ]

         base_commit -> commit2_base [ style = invis ]

         origin_branch -> origin_branch_new [ style = dashed ]
      }

      subgraph cluster_repo1 {
          label = "Local repo 1"
          base_commit0 [ shape = component, label = "Base commit" ]
          local_branch [ shape = invhouse, label = "branch", fontname = "monospace" ]
          commit1 [ shape = component, label = "Commit 1" ]
          commit2 [ shape = component, label = "Commit 2" ]
          local_branch_new [ shape = invhouse, label = "branch", fontname = "monospace" ]

          local_branch -> base_commit0 [ constraint = false ]
          base_commit0 -> commit1 [ arrowhead = inv ]
          commit1 -> commit2 [ arrowhead = inv ]
          local_branch_new -> commit2 [ constraint = false ]

          local_branch -> local_branch_new [ style = dashed, minlen = 2 ]
      }

      subgraph cluster_repo2 {
          label = "Local repo 2"
          commit2_2 [ shape = component, label = "Commit 2" ]
          local_branch2 [ shape = invhouse,  label = "branch", fontname = "monospace" ]

          local_branch2 -> commit2_2 [ constraint = false ]
      }

      base_commit -> base_commit0 [ label = "git pull", fontname = "monospace" ]
      commit2_base -> commit2_2 [ label = "git pull", fontname = "monospace" ]
      commit2 -> commit2_base [ label = <<table bgcolor="white" border="0" cellborder="0"><tr><td>git push</td></tr></table>>, fontname = "monospace" ]
   }


Forced push
+++++++++++

.. graphviz::

   digraph {
      subgraph cluster_baserepo {
         label = "Remote repo"
         base_commit [ shape = component, label = "Base commit" ]
         origin_branch [ shape = invhouse,  label = "origin/branch", fontname = "monospace" ]
         commit3_base  [ shape = component, label = "Commit 3", color = gray, fontcolor = gray  ]
         commit2_base  [ shape = component, label = "Commit 2" ]
         origin_branch_new [ shape = invhouse, label = "origin/branch", fontname = "monospace", color = gray, fontcolor = gray ]
         origin_branch_forced [ shape = invhouse, label = "origin/branch", fontname = "monospace" ]

         origin_branch -> base_commit [ constraint = false ]
         origin_branch_new -> commit3_base [ constraint = false, color = gray ]
         origin_branch_forced -> commit2_base [ constraint = false ]

         base_commit -> commit3_base [ style = invis ]
         commit3_base -> commit2_base [ style = invis ]

         origin_branch -> origin_branch_new [ style = dashed ]
         origin_branch_new -> origin_branch_forced [ style = dashed ]
      }

      subgraph cluster_repo1 {
          label = "Local repo 1"
          base_commit0 [ shape = component, label = "Base commit" ]
          local_branch [ shape = invhouse, label = "branch", fontname = "monospace" ]
          commit1 [ shape = component, label = "Commit 1" ]
          commit2 [ shape = component, label = "Commit 2" ]
          local_branch_new [ shape = invhouse, label = "branch", fontname = "monospace" ]

          local_branch -> base_commit0 [ constraint = false ]
          base_commit0 -> commit1 [ arrowhead = inv ]
          commit1 -> commit2 [ arrowhead = inv ]
          local_branch_new -> commit2 [ constraint = false ]

          local_branch -> local_branch_new [ style = dashed, minlen = 2 ]
      }

      subgraph cluster_repo2 {
          label = "Local repo 2"
          base_commit1 [ shape = component, label = "Base commit" ]
          local_branch2 [ shape = invhouse,  label = "branch", fontname = "monospace" ]
          commit3 [ shape = component, label = "Commit 3", color = gray, fontcolor = gray   ]
          local_branch_new2 [ shape = invhouse, label = "branch", fontname = "monospace", color = gray, fontcolor = gray   ]
          local_branch_forced2 [ shape = invhouse, label = "branch", fontname = "monospace" ]
          commit2_2 [ shape = component, label = "Commit 2"]

          base_commit1 -> commit3 [ arrowhead = inv, color = gray ]
          local_branch2 -> base_commit1 [ constraint = false ]
          local_branch2 -> local_branch_new2 [ style = dashed, minlen = 2 ]
          local_branch_new2 -> commit3 [ constraint = false, color = gray ]
          local_branch_forced2 -> commit2_2 [ constraint = false ]
          commit3 -> commit2_2 [ style = invis ]
          local_branch_new2 -> local_branch_forced2 [ style = dashed ]
      }

      base_commit -> base_commit0 [ label = "git pull", fontname = "monospace" ]
      base_commit -> base_commit1 [ label = "git pull", fontname = "monospace" ]
      commit3 -> commit3_base [ label = <<table bgcolor="white" border="0" cellborder="0"><tr><td>git push</td></tr></table>>, fontname = "monospace" ]
      commit2 -> origin_branch_new [ label = <<table bgcolor="white" border="0" cellborder="0"><tr><td>git push</td></tr></table>>, color = red, arrowhead = tee, fontname = "monospace" ]
      commit2 -> commit2_base [ label = "git push --force", fontname = "monospace" ]
      commit2_base -> commit2_2 [ label = <<table bgcolor="white" border="0" cellborder="0"><tr><td>git pull</td></tr></table>>, fontname = "monospace" ]
   }

Merge vs rebase
---------------

.. graphviz::

   digraph {
      node [ shape = component, fontname = "monospace" ]
      edge [ fontname = "monospace", labelfontname = "monospace" ]
      compound = true
      rankdir = LR
      subgraph cluster_old {
          margin = 16
          base_commit [ label = "Base commit" ]
          commit1 [ label = "Commit 1" ]
          commit2 [ label = "Commit 2" ]
          commit3 [ label = "Commit 3" ]
          commit4 [ label = "Commit 4" ]
          branch1 [ shape = invhouse, label = "stable" ]
          branch2 [ shape = invhouse, label = "devel" ]
          head [ shape = point, xlabel = "HEAD" ]

          commit1 -> base_commit
          commit2 -> commit1
          commit3 -> base_commit
          commit4 -> commit3

          branch1 -> commit2
          branch2 -> commit4
          head -> commit4
      }

      subgraph cluster_merged {
          base_commita [ label = "Base commit" ]
          commit1a [ label = "Commit 1" ]
          commit2a [ label = "Commit 2" ]
          commit3a [ label = "Commit 3" ]
          commit4a [ label = "Commit 4" ]
          merge [ label = "Merge commit" ]
          branch1a [ shape = invhouse, label = "stable" ]
          branch2a [ shape = invhouse, label = "devel" ]
          heada [ shape = point, xlabel = "HEAD" ]

          commit1a -> base_commita
          commit2a -> commit1a
          commit3a -> base_commita
          commit4a -> commit3a

          merge -> commit2a
          merge -> commit4a

          branch2a -> merge
          branch1a -> commit4a
          heada -> merge
      }

      command [ label = "git merge stable", shape = rarrow ]
      head -> command [ style = invis ]
      command -> heada [ style = invis ]

      subgraph cluster_rebased {
          base_commitb [ label = "Base commit" ]
          commit1b [ label = "Commit 1" ]
          commit2b [ label = "Commit 2" ]
          commit3b [ label = "Commit 3&dagger;" ]
          commit4b [ label = "Commit 4&dagger;" ]
          commit3bo [ label = "Commit 3", color = lightgray, fontcolor = lightgray ]
          commit4bo [ label = "Commit 4", color = lightgray, fontcolor = lightgray  ]
          branch1b [ shape = invhouse, label = "stable" ]
          branch2b [ shape = invhouse, label = "devel" ]
          headb [ shape = point, xlabel = "HEAD" ]

          commit1b -> base_commitb
          commit2b -> commit1b
          commit3b -> commit2b
          commit4b -> commit3b
          commit3bo -> base_commitb [ color = lightgray ]
          commit4bo -> commit3bo [ color = lightgray ]

          branch2b -> commit4b
          branch1b -> commit2b
          headb -> commit4b
      }

      command2 [ label = "git rebase stable", shape = rarrow ]
      head -> command2 [ style = invis ]
      command2 -> headb [ style = invis ]
   }


Distributed workflow with PRs
-----------------------------

.. graphviz::

   digraph {
      node [ shape = component ]
      edge [ fontname = "monospace", labelfontname = "monospace" ]
      rankdir = LR

      subgraph cluster_local {
         label = "Local repo"

         subgraph {
            rank = same
            local [ shape = "invhouse", label = "mybranch" ]
            base0 [ label = "Base commit" ]
            local -> base0 [ xlabel = <<table bgcolor="white" border="0" cellborder="0"><tr><td>git checkout -b mybranch</td></tr></table>> ]
         }

         commit1 [ label = "Commit 1" ]
         base0 -> commit1 [ arrowhead = inv, label = "git commit" ]
         commit1prime [ label = "Commit 1&dagger;" ]
         commit1 -> commit1prime [ label = "git commit --amend" ]
         commit1prime2 [ label = "Commit 1&Dagger;" ]
         commit1prime -> commit1prime2 [ label = "git commit --amend" ]
      }

      subgraph cluster_remote {
         label = "Remote repo"

         subgraph {
            rank = same
            base [ label = "Base commit" ]
            main [ shape = invhouse, label = "main", fontname = "monospace" ]
            main -> base
         }

         subgraph {
            rank = same
            userbranch [ shape = invhouse, label = "user/name/feature", fontname = "monospace" ]
            commit1a [ label = "Commit 1" ]
            userbranch -> commit1a
            pr [ shape = hexagon, label = "PR" ]
         }
         base -> commit1a [ arrowhead = inv ]

         subgraph {
            rank = same
            userbranch1 [ shape = invhouse, label = "user/name/feature", fontname = "monospace" ]
            commit1primea [ label = "Commit 1&dagger;" ]
            userbranch1 -> commit1primea
            pr0 [ shape = hexagon, label = "PR" ]
         }

         base -> commit1primea [ arrowhead = inv ]
         userbranch -> userbranch1 [ style = dotted ]
         pr -> pr0 [ style = dotted ]
         commit1a -> commit1primea [ style = dotted ]

         subgraph {
            rank = same
            userbranch2 [ shape = invhouse, label = "user/name/feature", fontname = "monospace" ]
            commit1prime2a [ label = "Commit 1&Dagger;" ]
            userbranch2 -> commit1prime2a
            pr1 [ shape = hexagon, label = "PR" ]
         }

         base -> commit1prime2a [ arrowhead = inv ]
         userbranch1 -> userbranch2 [ style = dotted ]
         commit1primea -> commit1prime2a [ style = dotted ]
         pr0 -> pr1 [ style = dotted ]

         subgraph {
            rank = same
            commit2a [ label = "Commit 2" ]
            commit1x [ label = "Commit 1&bull;" ]
            commit2a -> commit1x [ arrowhead = inv ]

            main2 [ shape = invhouse, label = "main", fontname = "monospace" ]
            main2 -> commit1x [ constraint = false ]
         }

         base -> commit2a [ arrowhead = inv ]
         main -> main2 [ style = dotted ]

         commit1prime2a -> commit1x [ style = invis ]
         commit1prime2a -> main2 [ style = invis ]

         commit1primea -> pr0 [ xlabel = "Update", labelfontname = "serif" ]
         commit1prime2a -> pr1 [ xlabel = "Update", fontname = "serif" ]
      }

      subgraph cluster_maintainer {
         label = "Maintainer's repo"
         margin = 16

         baseb [ label = "Base commit" ]
         commit2b [ label = "Commit 2" ]
         commit1prime3 [ label = "Commit 1&Dagger;" ]
         commit1prime4 [ label = "Commit 1&bull;" ]
         commit1prime3 -> commit1prime4 [ xlabel = "git rebase" ]
         baseb -> commit2b [ arrowhead = inv ]
         baseb -> commit1prime3 [ arrowhead = inv ]
         commit2b -> commit1prime4 [ arrowhead = inv ]
         userbranchb [ shape = invhouse, label = "feature", fontname = "monospace" ]

         userbranchb -> commit1prime3

         mainb [ shape = invhouse, label = "main", fontname = "monospace" ]
         mainb -> commit2b

         userbranchc [ shape = invhouse, label = "feature", fontname = "monospace" ]
         userbranchc -> commit1prime4

         userbranchb -> userbranchc [ style = dotted ]

         baseb -> userbranchb [ style = invis ]
      }

      base -> base0 [ label = "git pull" ]

      commit1 -> pr [ label = "Create a pull request", decorate = true ]

      commit1 -> commit1a [ label = "git push origin HEAD:user/name/feature", constraint = false, decorate = true ]
      commit1prime -> commit1primea [ label = "git push origin +HEAD:user/name/feature", constraint = false ]
      commit1prime2 -> commit1prime2a [ label = "git push origin +HEAD:user/name/feature", constraint = false ]

      commit2a -> commit2b [ label = "git pull", constraint = false, decorate = true ]
      commit1prime2a -> commit1prime3 [ label = "git pull", constraint = false ]
      commit1prime4 -> commit1x [ taillabel = "git push origin HEAD:main", constraint = false, labeldistance = 30, labelangle = 0 ]

      pr -> commit1prime [ label = <<table bgcolor="white" border="0" cellborder="0"><tr><td>Review notes</td></tr></table>>, fontname = "serif", constraint = false ]
      pr0 -> commit1prime2 [ label = <<table bgcolor="white" border="0" cellborder="0"><tr><td>Review notes</td></tr></table>>, fontname = "serif", constraint = false ]
      pr1 -> commit1prime3 [ taillabel = "Approve", fontname = "serif", constraint = false, labeldistance = 5, labelangle = -10 ]
   }
